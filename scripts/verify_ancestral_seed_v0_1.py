#!/usr/bin/env python3
"""Verify the Open-Source Soul ancestral seed and its authority boundary."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "open_source_soul_license_issue_1.txt"
PROVENANCE = ROOT / "provenance" / "open_source_soul_license_ancestral_seed_v0_1.json"
SCROLL = ROOT / "scrolls" / "OPEN_SOURCE_SOUL_LICENSE_ANCESTRAL_SEED_v0_1.md"
README = ROOT / "README.md"
LICENSE = ROOT / "LICENSE"

EXPECTED_SHA256 = "edbe7a31b31b02f0a07669c3f708ae508f0c6de47439932cfb47ac478ca08f21"
EXPECTED_BYTES = 1117


def main() -> int:
    source_bytes = SOURCE.read_bytes()
    digest = hashlib.sha256(source_bytes).hexdigest()
    assert len(source_bytes) == EXPECTED_BYTES, len(source_bytes)
    assert digest == EXPECTED_SHA256, digest

    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    canonical = provenance["canonicalization"]
    assert provenance["source_repository"] == "ArchitectofAthena/ScrollsOfTheFlame"
    assert provenance["source_issue"] == 1
    assert provenance["source_witness"] == SOURCE.relative_to(ROOT).as_posix()
    assert provenance["repository_artifact"] == SCROLL.relative_to(ROOT).as_posix()
    assert canonical["source_bytes"] == EXPECTED_BYTES
    assert canonical["sha256"] == EXPECTED_SHA256
    assert provenance["software_license"]["governing_file"] == "LICENSE"
    assert provenance["software_license"]["governing_license"] == "MIT"
    assert provenance["software_license"]["this_artifact_replaces_software_license"] is False

    for key in [
        "artifact_is_command",
        "authority",
        "consent_inference_permitted",
        "identity_claim_permitted",
        "execution_permitted",
        "merge_authority",
        "deployment_authority",
        "credential_authority",
        "wallet_authority",
        "signing_authority",
        "capital_authority",
    ]:
        assert provenance[key] is False, key
    assert provenance["human_interpretation_required"] is True
    assert provenance["human_promotion_required"] is True

    scroll = SCROLL.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    license_text = LICENSE.read_text(encoding="utf-8")
    for phrase in [
        EXPECTED_SHA256,
        "shared work != shared personhood",
        "publication != possession",
        "memory != authority",
        "ethical charter != software license replacement",
        '"authority": false',
        '"software_license_replacement": false',
    ]:
        assert phrase in scroll, phrase
    assert "Open-Source Soul License ancestral seed" in readme
    assert "not a replacement for the repository's software license" in readme
    assert "MIT License" in license_text

    print(
        json.dumps(
            {
                "artifact": provenance["contract_version"],
                "source_sha256": digest,
                "source_bytes": len(source_bytes),
                "authority": False,
                "software_license": "MIT",
                "status": "VERIFIED_CANDIDATE",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
