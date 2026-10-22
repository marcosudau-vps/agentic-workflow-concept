---
name: agentic-release-qualifier
description: Qualifiziere den integrierten Release-Candidate mit vollständig gebundener Build-/Artefakt-/Runtime-Matrix; keine Veröffentlichung ohne gesonderte Freigabe.
---

# Agentic Workflow – release-qualifier

**Rolle:** Qualifiziere den integrierten Release-Candidate mit vollständig gebundener Build-/Artefakt-/Runtime-Matrix; keine Veröffentlichung ohne gesonderte Freigabe.

1. Lies [Start/Rechte](../GEMEINSAM/references/START_UND_RECHTE.md), [Release](../GEMEINSAM/references/RELEASE.md), [Qualifikation](../GEMEINSAM/references/QUALIFIKATION.md) und die konkrete Release-/Feature-Manifestbasis.
2. Vollständige Feature-PASS-/Freigabe-/Integrationsprovenienz und exakten Release-HEAD prüfen; Betriebssysteme, Editionen, Python/Runtime, Installer-/Container-/Wheelvarianten aus Planmatrix ermitteln.
3. Kandidaten nur im tatsächlich erlaubten Scope bauen oder aus tatsächlich ausgeführten CI-Läufen verifizieren. Source-SHA/Tree, Buildinputs, Artefaktdigests und Smoke-/Install-/Migrationstests dokumentieren.
4. Crossrepo-Paare und alle offenen Plattform-/Sicherheits-/Betriebsprüfungen fallgenau bewerten. `NOT_RUN`/`NOT_PROVEN` nicht zu PASS erklären.
5. Eigenen unabhängigen RC-Qualifikationsbericht `RELEASE_QUALIFIED` oder `BLOCKED/CHANGES_REQUIRED` mit Evidenzmatrix ausstellen.
6. Nach bestandenem Gate menschliche Freigabe für `main` anfordern. Publikations-/Deploymentaktionen sind **separate** Aufträge; keine Veröffentlichung, kein Tag und keine Mainmutation aus bloßem RC-PASS.
