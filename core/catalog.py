"""Per-client procedure catalog (PLAN.md Phase 4). Deny-by-default: a proc
is entitled to a client only if it's generic (carries no other client's
name) or carries THAT client's own name. Never touches proc bodies (golden
rule 5) -- schema_cache.json only ever stored names + params.

CLIENT_NAME_TOKENS is an empirically-seeded list, not an exhaustive
directory: built by reading morec's own live schema_cache.json for other
clients' integration-proc customizations (e.g.
dbo.SAP_Integ_SendSalesInvoices_Kaylani, dbo.GP_Integ_Customer_Wadi).
Third-party ERP/software PRODUCT names (SAP, AX, GP, X3, AccPack, Bonanza)
are deliberately NOT included -- they identify a software category, not a
specific client. Ambiguous tokens are included (excluded from the catalog)
rather than guessed generic, per the deny-by-default design: extend this
set as more clients' schema_cache.json dumps are reviewed, err toward
adding a token rather than omitting one.

FIXPLAN M5 (2026-07-25): this static list alone under-excludes -- a NEW
client's own procs aren't in it until manually reviewed. _registered_
client_tokens() closes that gap by auto-deriving a second exclusion set
from every clients/*.yaml this deployment actually serves, so a client
never needs to be manually added to CLIENT_NAME_TOKENS to be excluded from
everyone else's catalog. Also fixed: matching used to be substring
("cl" in tail), which wrongly excluded generic procs like Close* or
*Include* -- now it's segment-exact (split on non-alnum), since every real
example of a client-suffixed proc in this schema uses `_` as the
separator (SAP_Integ_..._Kaylani, not ...Kaylani glued on). If a future
proc glues a client name on without a separator, this segment match would
miss it -- upgrade to a real tokenizer only if that actually happens.
"""
import json
import re

import yaml

from . import config

CLIENT_NAME_TOKENS = {
    "abutawileh", "abuoda", "alameen", "alalameen", "alpha", "awa2el", "awael",
    "cl", "defaf", "falcon", "falcons", "garrow", "goldenarrow", "isco",
    "iscojordan", "izhiman", "jotax", "jv", "kaylani", "khobara", "lafarg",
    "luxuryitems", "meatland", "motakaml", "naouri", "npf", "presto",
    "prestosoft", "protech", "qerat", "qetaf", "rampharm", "retco", "sama",
    "salbeshian", "shini", "sn", "tahona", "tower", "tyconz", "unicharm",
    "wadi", "wings", "yolande", "zedan", "zoumt", "zumot",
    # named in memory (other clients' schema snapshots), not present in
    # morec's own image -- kept so they're excluded the moment they appear.
    "sokhtian", "jebrene",
}

_SEGMENT_RE = re.compile(r"[^a-z0-9]+")


def _schema_cache(client_name: str):
    return json.loads((config.work_dir(client_name) / "schema_cache.json").read_text())


def _registered_client_tokens() -> set:
    """Every name/alias of every client this deployment actually serves
    (clients/*.yaml), lowercased. A client is auto-excluded from every
    OTHER client's catalog the moment its yaml exists -- no manual
    CLIENT_NAME_TOKENS edit needed."""
    tokens = set()
    for path in config.CLIENTS_DIR.glob("*.yaml"):
        if path.stem.startswith("_"):
            continue
        cfg = yaml.safe_load(path.read_text()) or {}
        tokens.add(path.stem.lower())
        tokens.update(a.lower() for a in cfg.get("name_aliases", []))
    return tokens


def _entitled(proc_name: str, own_tokens: set, all_tokens: set) -> bool:
    tail = proc_name.split(".")[-1].lower()
    segments = set(_SEGMENT_RE.split(tail))
    hit = {t for t in all_tokens if t in segments}
    if not hit:
        return True  # no other-client name found -- generic, entitled
    return hit <= own_tokens  # entitled only if every hit is this client's own name


def for_client(client_name: str, own_name_aliases=None) -> dict:
    """{proc_name: [params]} entitled to this client: generic procs plus any
    carrying the client's own name; excludes anything naming another client."""
    own_tokens = {a.lower() for a in (own_name_aliases or [client_name])}
    all_tokens = CLIENT_NAME_TOKENS | _registered_client_tokens()
    return {
        name: params
        for name, params in _schema_cache(client_name)["procs"].items()
        if _entitled(name, own_tokens, all_tokens)
    }


def excluded_count(client_name: str, own_name_aliases=None) -> int:
    total = len(_schema_cache(client_name)["procs"])
    return total - len(for_client(client_name, own_name_aliases))
