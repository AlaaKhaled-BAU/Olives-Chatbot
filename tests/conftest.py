"""Pytest setup — pin CHATBOT_CLIENT before api.server import."""
import os
from unittest.mock import patch

os.environ.setdefault("CHATBOT_CLIENT", "morec")

# Tenant pack live probes call sql.run_select; keep agent tests deterministic.
patch("core.tenant_pack._live_facts", return_value={}).start()
