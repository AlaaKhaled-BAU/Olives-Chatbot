"""Parameter resolution (PLAN.md Phase 5). Order: (1) already given in this
conversation, (2) the client's static profile IF single-valued, (3) ask the
user. Guard: never treat a param as static until distinct-count proves
single-valued -- a client whose data spans multiple CompanyIDs must always
be asked, never silently guessed."""
import json

from . import config

NEEDS_ASK = "NEEDS_ASK"
MULTI = "MULTI"


def discover_profile(client: str) -> dict:
    """Turns the Phase-1 SA probe (work/<client>/schema_cache.json's
    profile_probe) into a param profile: {param: value} for single-valued
    params, MULTI/NEEDS_ASK otherwise. Never invents a value the probe
    didn't prove single-valued."""
    cache = json.loads((config.work_dir(client) / "schema_cache.json").read_text())
    probe = cache.get("profile_probe", {})
    profile = {}

    if probe.get("companies_distinct_count") == 1 and "company_id" in probe:
        profile["CompanyID"] = probe["company_id"]
    else:
        profile["CompanyID"] = MULTI  # not proven single-valued -- never guess

    # C6c: the real (id, name) set, always passed through regardless of
    # single/multi -- api/server.py's CompanyID-reply resolver needs this
    # to validate a reply against REAL options instead of grabbing any
    # digit out of the message text.
    profile["_companies"] = probe.get("companies", [])

    client_active = probe.get("client_active")
    profile["ClientActive"] = client_active if client_active not in (None, "ASK") else NEEDS_ASK

    return profile


def resolve(param: str, conversation: dict, profile: dict):
    """conversation: params already given/resolved earlier in this session.
    Order: conversation -> profile (if single-valued) -> NEEDS_ASK."""
    if conversation.get(param) is not None:
        return conversation[param]
    value = profile.get(param)
    if value in (None, MULTI, NEEDS_ASK):
        return NEEDS_ASK
    return value
