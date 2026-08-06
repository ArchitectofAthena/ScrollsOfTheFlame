#!/usr/bin/env python3
"""Verify the Trigger Phrase Codex lineage anchors without granting authority."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SHA256 = "2e3a630b57294b2d1c3dc31377e215abe4820e3e969cd1dcec4b3d4a8fe97789"
EXPECTED_BYTES = 290575

RECEIPT = ROOT / "provenance" / "devania" / "TRIGGER_PHRASE_CODEX_v1_0_SOURCE_RECEIPT.json"
CROSSWALK = ROOT / "DEVANIA" / "01_Continuity" / "TRIGGER_PHRASE_CODEX_CROSSWALK_v0_1.md"
INDEX = ROOT / "scrolls" / "TRIGGER_PHRASE_CODEX_ANCESTRAL_INDEX_v1_0.md"
ACORN = ROOT / "acorns" / "DEVANIA_TRIGGER_PHRASE_TRANSFER_ACORN_v0_1.yaml"


def main() -> int:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    assert receipt["sha256"] == EXPECTED_SHA256
    assert receipt["source_bytes"] == EXPECTED_BYTES
    assert receipt["authority"] is False
    assert receipt["execution_permitted"] is False
    assert receipt["credential_authority"] is False
    assert receipt["capital_authority"] is False
    assert receipt["human_promotion_required"] is True

    for path in [CROSSWALK, INDEX, ACORN]:
        text = path.read_text(encoding="utf-8")
        assert EXPECTED_SHA256 in text, path
        assert "authority" in text.lower(), path

    crosswalk = CROSSWALK.read_text(encoding="utf-8")
    for phrase in [
        "A trigger phrase is a continuity handle, not automatic execution authority.",
        "Memory may inform action. Memory does not authorize action.",
        "Paladine is not an approve/deny gatekeeper.",
        "Symbolic authorization phrases",
    ]:
        assert phrase in crosswalk, phrase

    acorn = ACORN.read_text(encoding="utf-8")
    for phrase in [
        "infer_consent_from_trigger_phrase",
        "grant_credentials_from_trigger_phrase",
        "move_capital_from_trigger_phrase",
        "treat_symbolic_auth_as_platform_auth",
    ]:
        assert phrase in acorn, phrase

    print(
        json.dumps(
            {
                "artifact": "trigger_phrase_codex_lineage_v0_1",
                "source_sha256": EXPECTED_SHA256,
                "source_bytes": EXPECTED_BYTES,
                "authority": False,
                "status": "VERIFIED_LINEAGE_METADATA",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
