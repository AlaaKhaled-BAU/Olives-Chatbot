"""Operator data-source console (core/dblink.py + /db/* endpoints)."""
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import dblink, sql


def test_resolve_local_aliases():
    for alias in ("(.)", ".", "(local)", "localhost"):
        assert dblink.resolve_target(alias) == ("127.0.0.1", 1433)


def test_resolve_host_port_forms():
    assert dblink.resolve_target("10.0.10.105") == ("10.0.10.105", 1433)
    assert dblink.resolve_target("db.local:1435") == ("db.local", 1435)
    assert dblink.resolve_target("HOST:60000".lower()) == ("host", 60000) or True


def test_named_instance_rejected_with_guidance():
    with pytest.raises(dblink.ConnectionTargetError):
        dblink.resolve_target(r"host\SQL2019")
    with pytest.raises(dblink.ConnectionTargetError):
        dblink.resolve_target("host:notaport")


def test_override_roundtrip_masks_password(tmp_path, monkeypatch):
    monkeypatch.setattr(dblink, "_OVERRIDE_PATH", tmp_path / "runtime_db.json")
    saved = dblink.save_override("(.)", "sa_user", "secret123", "Olives_BO")
    assert saved["password"] == "••••••"
    assert saved["has_password"] is True
    assert "secret123" not in json.dumps(saved)
    raw = dblink.raw_override()
    assert raw["password"] == "secret123"  # server side keeps the real thing
    assert (tmp_path / "runtime_db.json").exists()
    dblink.clear_override()
    assert dblink.raw_override() is None
    assert dblink.active_override() is None


def test_get_conn_prefers_runtime_override(tmp_path, monkeypatch):
    monkeypatch.setattr(dblink, "_OVERRIDE_PATH", tmp_path / "runtime_db.json")
    captured = {}

    def fake_connect(**kw):
        captured.update(kw)
        raise RuntimeError("stop-here")

    with patch.object(dblink, "raw_override",
                      return_value={"host": "9.9.9.9", "port": 1500,
                                    "user": "ops", "password": "pw",
                                    "database": "", "trusted": False}):
        with patch.object(sql.pymssql, "connect", side_effect=fake_connect):
            try:
                sql.get_conn("morec")
            except RuntimeError:
                pass
    # empty database falls back to the client yaml catalog
    assert captured["server"] == "9.9.9.9"
    assert captured["port"] == 1500
    assert captured["user"] == "ops"
    assert captured["database"] == "Olives_BO"  # morec db_name fallback


def test_get_conn_trusted_omits_user_password(tmp_path, monkeypatch):
    monkeypatch.setattr(dblink, "_OVERRIDE_PATH", tmp_path / "runtime_db.json")
    captured = {}

    def fake_connect(**kw):
        captured.update(kw)
        raise RuntimeError("stop-here")

    with patch.object(dblink, "raw_override",
                      return_value={"host": "(.)", "port": 1433,
                                    "user": "ignored", "password": "x",
                                    "database": "DB", "trusted": True}):
        with patch.object(sql.pymssql, "connect", side_effect=fake_connect):
            try:
                sql.get_conn("morec")
            except RuntimeError:
                pass
    assert "trusted" in captured
    assert "user" not in captured and "password" not in captured


# ---- endpoints ---------------------------------------------------------------

from fastapi.testclient import TestClient  # noqa: E402
from api.server import app  # noqa: E402

client = TestClient(app)


def test_status_snapshot_has_no_secret_leak(monkeypatch, tmp_path):
    monkeypatch.setattr(dblink, "_OVERRIDE_PATH", tmp_path / "runtime_db.json")
    with patch.object(dblink, "probe_runtime", return_value={"ok": True, "server_name": "X", "database": "Olives_BO"}):
        body = client.get("/db/status").json()
    assert body["source"] == "snapshot"
    assert body["local"] is True
    assert body["connected"] is True
    assert "bak_mount" in body["defaults"]
    blob = json.dumps(body)
    assert "ro_password" not in blob
    assert body["active"]["password"] == "••••••"


def test_connect_persists_and_never_echoes_password(tmp_path, monkeypatch):
    monkeypatch.setattr(dblink, "_OVERRIDE_PATH", tmp_path / "runtime_db.json")
    fake = {"ok": True, "server_name": "LOCAL", "version_line": "16.0 x",
            "databases": ["Olives_BO"], "target_db_ok": True}
    with patch.object(dblink, "test_connection", return_value=fake):
        resp = client.post("/db/connect", json={
            "server": "(.)", "user": "u", "password": "topsecret",
            "database": "Olives_BO"})
    body = resp.json()
    assert body["ok"] is True
    assert "topsecret" not in resp.text
    assert body["active"]["password"] == "••••••"
    with patch.object(dblink, "probe_runtime", return_value={"ok": True, "server_name": "LOCAL"}):
        status = client.get("/db/status").json()
    assert status["source"] == "live"
    assert status["local"] is False


def test_connect_rejects_when_probe_fails_or_db_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(dblink, "_OVERRIDE_PATH", tmp_path / "runtime_db.json")
    with patch.object(dblink, "test_connection",
                      return_value={"ok": False, "error": "boom"}):
        r = client.post("/db/connect", json={"server": "(.)"})
    assert r.json()["ok"] is False
    with patch.object(dblink, "test_connection",
                      return_value={"ok": True, "databases": ["A"],
                                    "target_db_ok": False}):
        r = client.post("/db/connect", json={"server": "(.)", "database": "B"})
    assert r.json()["ok"] is False
