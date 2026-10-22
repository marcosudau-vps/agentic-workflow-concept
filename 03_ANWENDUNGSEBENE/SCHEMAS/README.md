# Projektbezogene maschinenlesbare Schemas

Die JSON-Schemas modellieren die aktuell beschriebenen Verfahrensdaten, nicht die eigentliche Fachabnahme. Ein Schema-PASS für einen `ROOT_PASS`-String ist ausdrücklich **kein** Beweis für einen fachlich gültigen ROOT_PASS. Das mitgelieferte offline Prüfsystem verwendet die Python-Standardbibliothek und prüft zentrale Pflichtfelder; bei vorhandenem `jsonschema`-Paket kann ein Projekt zusätzlich alle Schema-Features vollständig validieren.

| Schema | Muster |
| --- | --- |
| [workflow-status](workflow-status.schema.json) | `VORLAGEN/TRACKING/WORKFLOW_STATUS.json` |
| [plan-status](plan-status.schema.json) | `VORLAGEN/PLANUNG/PLAN_STATUS.json` |
| [requirements](requirements.schema.json) | `VORLAGEN/PLANUNG/TRACEABILITY/requirements.json` |
| [package-manifest](package-manifest.schema.json) | `VORLAGEN/PLANUNG/EVIDENCE/package-manifest.json` |
| [feature-status](feature-status.schema.json) | `VORLAGEN/TRACKING/FEATURE_STATUS.json` |
| [release-matrix](release-matrix.schema.json) | `VORLAGEN/RELEASE/RC_MATRIX.json` |
| [finding](finding.schema.json) | Format für tatsächliche unabhängige Findings |
