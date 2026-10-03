"""Structured tracing (PLAN.md Phase 6): one JSONL line per turn, plus
Prometheus counters that Phase 7's /metrics endpoint exposes.

FIXPLAN M10 (2026-07-25): PLAN.md's Phase 7 acceptance named five metrics
(request count, latency, cache-hit ratio, gate rejections, refusals) but
only REQUESTS (a proxy for count+refusals via its event label) ever got
built. Added the other three here, kept as the sole owner of Prometheus
wiring -- core/agent.py calls these functions, never touches a Counter/
Histogram object directly, same encapsulation as log_event()."""
import json
import subprocess
import time
from pathlib import Path

from prometheus_client import Counter, Histogram

TRACE_PATH = Path(__file__).resolve().parent.parent / "work" / "trace.jsonl"
_REPO = TRACE_PATH.parent.parent
_PREFIX_HASHES: dict[str, str] = {}


def _git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_REPO, text=True, stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


GIT_SHA = _git_sha()


def note_prefix_hash(client: str, prefix_hash: str) -> None:
    """Last stable-prefix hash built for this client in this process.
    log_event stamps it on every later line for that client."""
    _PREFIX_HASHES[client] = prefix_hash

REQUESTS = Counter("chatbot_requests_total", "Total agent turns", ["client", "event"])
TURN_LATENCY = Histogram("chatbot_turn_latency_seconds", "Agent turn latency", ["client"])
CACHE_HITS = Counter("chatbot_cache_hits_total", "Plan-cache hits", ["client"])
GATE_REJECTIONS = Counter("chatbot_gate_rejections_total", "SQL gate rejections", ["client"])
TABLE_USES = Counter(
    "chatbot_table_uses_total",
    "Business tables referenced by executed SQL (plan TRACK B: schema-trimming evidence)",
    ["client", "table"],
)


def record_table_uses(client: str, tables) -> None:
    """Count every t.* table an executed query referenced. Bounded label
    space (~450 views per client); fuels the keep-full-schema-vs-hybrid
    decision with data instead of taste."""
    for table in set(tables or []):
        TABLE_USES.labels(client=client, table=table).inc()


def observe_latency(client: str, seconds: float) -> None:
    TURN_LATENCY.labels(client=client).observe(seconds)


def record_cache_hit(client: str) -> None:
    CACHE_HITS.labels(client=client).inc()


def record_gate_rejection(client: str) -> None:
    GATE_REJECTIONS.labels(client=client).inc()


def log_event(client: str, question: str, event: str, subject: str | None = None, **fields):
    """event: one of 'answer', 'refused', 'needs_ask', 'feedback_negative'
    (C3: a thumbs-down, recorded for review -- see api/server.py's
    /feedback). `subject` (FIXPLAN M4) is a short hash identifying the
    caller (derived from their bearer token by api/server.py) -- never the
    raw token itself, so a leaked trace file can't be replayed as a
    credential."""
    TRACE_PATH.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "ts": time.time(), "client": client, "subject": subject,
        "question": question, "event": event,
        "git_sha": GIT_SHA,
        "prefix_hash": _PREFIX_HASHES.get(client),
        **fields,
    }
    with TRACE_PATH.open("a") as f:
        f.write(json.dumps(record, default=str) + "\n")
    REQUESTS.labels(client=client, event=event).inc()
