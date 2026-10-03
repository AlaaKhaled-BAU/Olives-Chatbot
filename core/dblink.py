"""Runtime data-source console (operator feature): point the chatbot at any
SQL Server from the UI without touching .env — mirroring the drift-tool's
connection model (reverse-engineered: per-side {server, db, user, password,
auth-type}, `.` = local default instance, databases listed via GetSchema)
with two upgrades: credentials persist 0600 inside gitignored work/ (their
.config stored plaintext), and passwords never travel back to the browser.

Precedence in core/sql.get_conn: runtime override > .env snapshot.
"""
import json
import os
import stat
from pathlib import Path

import pymssql

_OVERRIDE_PATH = Path(__file__).resolve().parent.parent / "work" / "runtime_db.json"


def _override_path() -> Path:
    if _OVERRIDE_PATH != Path(__file__).resolve().parent.parent / "work" / "runtime_db.json":
        return _OVERRIDE_PATH
    env_work = os.environ.get("CHATBOT_WORK_DIR")
    if env_work:
        return Path(env_work) / "runtime_db.json"
    return _OVERRIDE_PATH


_LOCAL_ALIASES = {".", "(.)", "(local)", "local", "localhost"}
_DEFAULT_PORT = 1433


class ConnectionTargetError(ValueError):
    """Raised when the server string can't be resolved to host:port."""


def resolve_target(raw_server: str) -> tuple[str, int]:
    """'(.)' -> local default instance. 'host:port' and bare host supported;
    named instances ('host\\SQL2019') need an explicit port because TDS
    instance resolution uses UDP 1434 browsing we don't implement."""
    raw = (raw_server or "").strip()
    if not raw:
        raise ConnectionTargetError("اسم الخادم مطلوب")
    if raw.lower() in _LOCAL_ALIASES:
        return "127.0.0.1", _DEFAULT_PORT
    if "\\" in raw:
        raise ConnectionTargetError(
            "المثيلات المسماة غير مدعومة — أدخل المنفذ صراحةً بصيغة host:port")
    if ":" in raw:
        host, _, port = raw.rpartition(":")
        if not port.isdigit():
            raise ConnectionTargetError("المنفذ يجب أن يكون رقماً")
        return host or "127.0.0.1", int(port)
    return raw, _DEFAULT_PORT


def test_connection(server: str, user: str, password: str,
                    database: str | None = None, port: int | None = None,
                    trusted: bool = False, timeout: float = 6.0) -> dict:
    """Probe a server WITHOUT persisting anything: identity, version line,
    and the databases this login can actually read (drift-tool's GetSchema
    equivalent). Returns a JSON-safe diagnostics dict."""
    host, resolved_port = resolve_target(server)
    if port:
        resolved_port = int(port)
    kwargs = dict(
        server=host, port=resolved_port,
        timeout=timeout, login_timeout=max(3, int(timeout)),
    )
    if not trusted:
        if not user:
            return {"ok": False, "error": "اسم المستخدم مطلوب"}
        kwargs.update(user=user, password=password or "")
    if database:
        kwargs["database"] = database
    try:
        conn = pymssql.connect(**kwargs)
    except pymssql.OperationalError as e:
        return {"ok": False, "host": host, "port": resolved_port,
                "error": _friendly_login_error(str(e))}
    except Exception as e:  # noqa: BLE001 — surface driver quirks verbatim-classified
        return {"ok": False, "host": host, "port": resolved_port,
                "error": _friendly_login_error(str(e))}
    try:
        cur = conn.cursor(as_dict=True)
        cur.execute("SELECT @@SERVERNAME AS server_name, @@VERSION AS version_line")
        ident = cur.fetchone()
        dbs: list[str] = []
        try:
            cur.execute(
                "SELECT name FROM sys.databases WHERE HAS_DBACCESS(name)=1 "
                "AND state=0 AND name NOT IN ('master','tempdb','model','msdb') "
                "ORDER BY name")
            dbs = [r["name"] for r in cur.fetchall()]
        except Exception:  # noqa: BLE001 — version-dependent view, non-fatal
            pass
        return {
            "ok": True, "host": host, "port": resolved_port,
            "server_name": ident["server_name"],
            "version_line": (ident["version_line"] or "")[:120],
            "databases": dbs,
            "target_db_ok": (database in dbs) if database else None,
        }
    finally:
        conn.close()


def _friendly_login_error(raw: str) -> str:
    low = raw.lower()
    if "login failed" in low or "18456" in low:
        return "فشل تسجيل الدخول — تحقق من اسم المستخدم وكلمة المرور"
    if "timed out" in low or "timeout" in low:
        return "انتهت المهلة — تحقق من العنوان والمنفذ وجدار الحماية"
    if "adaptive server is unavailable" in low or "connection refused" in low or "20009" in low:
        return "تعذر الوصول للخادم — تأكد من IP والمنفذ وأن الخدمة تعمل"
    return raw[:160]


def save_override(server: str, user: str, password: str, database: str,
                  port: int | None = None, trusted: bool = False) -> dict:
    host, resolved_port = resolve_target(server)
    payload = {
        "host": host, "port": int(port) if port else resolved_port,
        "user": user, "password": password or "",
        "database": database, "trusted": bool(trusted),
        "saved_at_epoch": __import__("time").time(),
    }
    p = _override_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload))
    try:
        os.chmod(p, stat.S_IRUSR | stat.S_IWUSR)  # 0600
    except OSError:
        pass
    return active_override()


def active_override() -> dict | None:
    try:
        data = json.loads(_override_path().read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    safe = dict(data)
    safe["password"] = "••••••"  # never round-trip secrets to the browser
    safe["has_password"] = bool(data.get("password"))
    return safe


def raw_override() -> dict | None:
    try:
        return json.loads(_override_path().read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def clear_override() -> None:
    try:
        _override_path().unlink()
    except FileNotFoundError:
        pass


def snapshot_defaults(client: str) -> dict:
    from . import config
    return {
        "host": os.environ.get("DB_HOST", "127.0.0.1"),
        "port": int(os.environ.get("DB_PORT", "1433")),
        "user": "chatbot_ro",
        "password": "••••••",
        "database": config.load_client(client)["db_name"],
        "bak_mount": os.environ.get("SQL_SNAPSHOT_MOUNT", "/snapshots"),
    }


def probe_runtime(client: str) -> dict:
    """Live ping of whatever get_conn() currently targets."""
    from . import sql
    try:
        conn = sql.get_conn(client)
    except FileNotFoundError:
        return {"ok": False, "error": "لا توجد كلمة مرور محلية (work/ro_password.txt)"}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": _friendly_login_error(str(e))}
    try:
        cur = conn.cursor(as_dict=True)
        cur.execute("SELECT @@SERVERNAME AS server_name, DB_NAME() AS database_name")
        row = cur.fetchone() or {}
        return {
            "ok": True,
            "server_name": row.get("server_name"),
            "database": row.get("database_name"),
        }
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": _friendly_login_error(str(e))}
    finally:
        try:
            conn.close()
        except Exception:  # noqa: BLE001
            pass
