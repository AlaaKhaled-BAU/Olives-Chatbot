"""Phase 3 acceptance: key custody + gateway completion + cache hit.
Requires the gateway running (gateway/README.md) -- skips if unreachable."""
import sys
from pathlib import Path

import pytest

CORE_DIR = Path(__file__).resolve().parent.parent / "core"
GATEWAY_ENV = Path(__file__).resolve().parent.parent / "gateway" / ".env"
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def test_no_secret_values_in_core():
    """The actual key VALUES from gateway/.env must never appear in core/ source."""
    secrets = []
    if GATEWAY_ENV.exists():
        for line in GATEWAY_ENV.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                _, _, value = line.partition("=")
                value = value.strip()
                if value:
                    secrets.append(value)
    for path in CORE_DIR.glob("*.py"):
        text = path.read_text()
        for secret in secrets:
            assert secret not in text, f"secret value leaked into {path}"


def test_completion_via_gateway_and_cache_hit():
    from core import llm
    try:
        r1 = llm.complete([{"role": "user", "content": "phase3-cache-check"}])
    except Exception as e:  # noqa: BLE001 - gateway may not be running in this environment
        pytest.skip(f"gateway not reachable: {e}")
    r2 = llm.complete([{"role": "user", "content": "phase3-cache-check"}])
    assert r1.choices[0].message.content == r2.choices[0].message.content, (
        "identical back-to-back requests should hit the gateway cache and return "
        "byte-identical content, not two independent generations"
    )
