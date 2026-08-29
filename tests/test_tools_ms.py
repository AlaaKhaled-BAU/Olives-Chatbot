"""tools_ms timing on agent tool wrap."""
import os
import sys
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("CHATBOT_CLIENT", "morec")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import agent


def test_tool_wrap_records_elapsed_ms():
    """Unit test of the monotonic wrap around _run_tool (plan Lane B)."""
    state = {"tools_ms": {}}
    name = "search_docs"

    def fake_run_tool(*args, **kwargs):
        return {}

    with patch.object(agent.time, "monotonic", side_effect=[100.0, 100.05]), \
         patch.object(agent, "_run_tool", side_effect=fake_run_tool):
        t0 = agent.time.monotonic()
        try:
            agent._run_tool(name, {}, {}, [], [], 1, "morec", state)
        finally:
            ms = int((agent.time.monotonic() - t0) * 1000)
            state["tools_ms"][name] = state["tools_ms"].get(name, 0) + ms

    assert 49 <= state["tools_ms"]["search_docs"] <= 50
