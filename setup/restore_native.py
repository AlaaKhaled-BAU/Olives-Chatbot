"""RESTORE a .bak into the native / production-like SQL Server instance."""
import os
import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_connect  # noqa: E402


def _poll_restore_progress(db_name: str, log, stop_event: threading.Event):
    try:
        conn = db_connect.sa_connect(as_dict=True)
        cur = conn.cursor()
        while not stop_event.is_set():
            cur.execute(
                "SELECT percent_complete FROM sys.dm_exec_requests "
                "WHERE command IN ('RESTORE DATABASE','RESTORE') AND session_id <> @@SPID"
            )
            rows = cur.fetchall()
            if rows and rows[0]["percent_complete"]:
                log(f"  restoring {db_name}: {rows[0]['percent_complete']:.0f}%")
            time.sleep(3)
        conn.close()
    except Exception:  # noqa: BLE001
        pass


def _wait_for_online(db_name: str, log, timeout: int = 900) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            conn = db_connect.sa_connect(as_dict=True)
            cur = conn.cursor()
            cur.execute("SELECT state_desc FROM sys.databases WHERE name = %s", (db_name,))
            row = cur.fetchone()
            conn.close()
            if row and row["state_desc"] == "ONLINE":
                return True
            if row:
                log(f"  [{db_name}] state={row['state_desc']}, still waiting...")
        except Exception as e:  # noqa: BLE001
            log(f"  poll error (will retry): {e}")
        time.sleep(5)
    return False


def restore_backup(bak_host_path: Path, db_name: str, log) -> dict:
    sql_path = db_connect.bak_to_sql_disk_path(bak_host_path)
    conn = db_connect.sa_connect(as_dict=True)
    cur = conn.cursor()

    log(f"reading backup header: {bak_host_path.name} (SQL path: {sql_path})")
    cur.execute(f"RESTORE HEADERONLY FROM DISK = '{sql_path}'")
    header = cur.fetchone()
    backup_date = header.get("BackupStartDate")
    sw_version = header.get("SoftwareVersionMajor")
    log(f"  backup taken {backup_date}, engine major version {sw_version}")

    cur.execute(f"RESTORE FILELISTONLY FROM DISK = '{sql_path}'")
    files = cur.fetchall()

    data_dir = os.environ.get("SQL_DATA_DIR", "/var/opt/mssql/data")
    move_clauses = []
    for f in files:
        logical = f["LogicalName"]
        is_log = f.get("Type") == "L"
        ext = "ldf" if is_log else "mdf"
        target = f"{data_dir}/{db_name}__{logical}.{ext}"
        move_clauses.append(f"MOVE '{logical}' TO '{target}'")
    moves_sql = ", ".join(move_clauses)

    log(f"restoring -> database [{db_name}] ({len(files)} file(s))")
    stop_event = threading.Event()
    progress_thread = threading.Thread(
        target=_poll_restore_progress, args=(db_name, log, stop_event), daemon=True
    )
    progress_thread.start()
    client_error = None
    try:
        cur.execute(
            f"RESTORE DATABASE [{db_name}] FROM DISK = '{sql_path}' "
            f"WITH {moves_sql}, REPLACE, RECOVERY, STATS = 5"
        )
    except Exception as e:  # noqa: BLE001
        client_error = e
    finally:
        stop_event.set()
        progress_thread.join(timeout=5)
    conn.close()

    if client_error is not None:
        log(f"  restore connection dropped ({client_error}); checking server-side state...")
        if not _wait_for_online(db_name, log):
            raise RuntimeError(f"RESTORE failed for {bak_host_path.name}: {client_error}")

    log(f"restored [{db_name}].")
    return {"backup_date": str(backup_date), "engine_major_version": sw_version}
