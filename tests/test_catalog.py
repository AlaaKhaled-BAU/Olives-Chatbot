"""FIXPLAN M5: catalog deny-by-default must (a) auto-exclude every
registered client's own procs from every OTHER client's catalog with zero
manual CLIENT_NAME_TOKENS edits, and (b) match on whole name segments, not
substrings (the old "cl" in tail check wrongly excluded generic procs like
Pro_GetCashCloseTotals). Uses morec's real schema_cache.json -- no DB/LLM
dependency, so this runs fast and offline."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import catalog, config

OWN = {"morec", "morek"}


def _all_tokens():
    return catalog.CLIENT_NAME_TOKENS | catalog._registered_client_tokens()


def test_known_cross_client_proc_is_excluded():
    assert not catalog._entitled("dbo.CL_Integ_SendAllTransactions", OWN, _all_tokens())


def test_segment_match_no_longer_false_positives_on_substring():
    """These are generic procs whose name merely CONTAINS "cl" as a
    substring (…Close…, …Class…) -- the old substring check wrongly
    excluded all of them; segment-exact match must not."""
    generic_procs = [
        "dbo.Pro_GetCashCloseTotals",
        "dbo.Pro_UnCloseOrder",
        "dbo.Rpt_CustomerClassChange",
        "dbo.Pro_CustomersClass",
    ]
    all_tokens = _all_tokens()
    for proc in generic_procs:
        assert catalog._entitled(proc, OWN, all_tokens), f"{proc} wrongly excluded"


def test_new_client_yaml_is_auto_excluded_with_zero_code_changes():
    """Registering a brand-new client (just a clients/*.yaml, no
    CLIENT_NAME_TOKENS edit) must be enough to exclude its named procs from
    every other client's catalog."""
    ghost_path = config.CLIENTS_DIR / "ghosttest.yaml"
    ghost_path.write_text(
        "db_name: chatbot_db_ghost\ncompany_scope: single\n"
        "name_aliases: [ghosttest, ghostcorp9000]\nlocale: ar\napi_token: test-only\n"
    )
    try:
        all_tokens = _all_tokens()
        assert "ghostcorp9000" in all_tokens
        fake_proc = "dbo.SAP_Integ_SendInvoices_GhostCorp9000"
        assert not catalog._entitled(fake_proc, OWN, all_tokens)
        assert catalog._entitled(fake_proc, {"ghosttest", "ghostcorp9000"}, all_tokens)
    finally:
        ghost_path.unlink()


def test_morec_catalog_excludes_no_registered_sibling_client():
    """End-to-end for_client(): morec's real catalog must not contain any
    proc naming rukn (the other client actually registered right now)."""
    rukn_aliases = config.load_client("rukn")["name_aliases"]
    entitled = catalog.for_client("morec", ["morec", "morek"])
    for alias in rukn_aliases:
        low = alias.lower()
        assert not any(low in name.lower() for name in entitled), (
            f"morec's catalog contains a proc naming rukn alias {alias!r}"
        )
