# Devania Source Intake

This directory preserves Devania source witnesses before interpretation or promotion.

Use it for supplied:

- community blueprints;
- government structures and constitutions;
- solar and agrovoltaic plans;
- resilient-node diagrams;
- images and renders;
- notes, exports, transcripts, and random thoughts;
- spreadsheets, calculations, and site assumptions;
- prior versions that must remain traceable.

## Intake rules

1. Preserve the original file unchanged when possible.
2. Record its original filename, date received, author or source, license/permission basis, and privacy classification.
3. Compute SHA-256 after the byte-preserved source is available.
4. Do not silently correct, reconcile, or merge contradictions in the source witness.
5. Place interpretation, cleaned text, and promoted descendants in `DEVANIA/`, not over the source.
6. Mark anything containing private locations, resident data, credentials, security details, medical information, or culturally sensitive material as private and do not commit it to this public repository.

## Suggested layout

```text
sources/devania/
├── blueprints/
├── governance/
├── solar_agrovoltaics/
├── images/
├── notes/
├── transcripts/
└── manifests/
```

## Source manifest minimum

Each source should eventually have a manifest containing:

- `source_id`
- `original_filename`
- `received_at`
- `author_or_source`
- `description`
- `privacy_classification`
- `license_or_permission`
- `sha256`
- `source_bytes`
- `derived_artifacts`
- `authority: false`
- `human_promotion_required: true`

Source preservation is not adoption.
