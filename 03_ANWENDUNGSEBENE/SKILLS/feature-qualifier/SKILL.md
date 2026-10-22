---
name: agentic-feature-qualifier
description: Prüfe eine in sich abgeschlossene Feature-Gesamtfassung gegen den eingefrorenen Plan, die angenommenen Arbeitspakete und echte Integrations-/Auslieferungsbelege.
---

# Agentic Workflow – unabhängiger Featurequalifier

1. Lies [Start/Rechte](../GEMEINSAM/references/START_UND_RECHTE.md), [Featuregate](../GEMEINSAM/references/FEATURE_GATE.md), [Qualifikation](../GEMEINSAM/references/QUALIFIKATION.md) und die konkrete Feature-/Releasebaseline.
2. Stelle exakte Feature-Head-/Tree-/Parentidentität sowie jede abgeschlossene AP-Aggregation samt unabhängigem `ROOT_PASS`, menschlichem Übernahmeprompt und wirklichem Tree-/Mergebeweis fest.
3. Prüfe den **gesamten Featureumfang**, übergreifende Architektur-, Datenfluss-, Vertrags- und Migrationskohärenz, reale Integration, Build-/Install-/Runtime-Checks, Dokumentation und sämtliche Pflichten aus dem Featurevertrag; nicht lediglich einzelne frühere Paket-PASS-Berichte addieren.
4. Frühere Pflichtfindings/Scopegrenzen und unabhängige Test-/Runtimebelege vollständig erfassen; neue Integrationslücken als präzise Findings mit Owner/Anforderung/Repro ausweisen.
5. In eigener frischer Runakte `FEATURE_ROOT_PASS` nur ohne offene Featurepflichten erteilen, andernfalls `FEATURE_CHANGES_REQUIRED/BLOCKED`. Keine Produktfixes und keine Freigabe des eigenen Werks.
6. Nach bestandenem Gate `FEATURE_WAITING_FOR_APPROVAL` melden. Die Aufnahme als genau ein Aggregat in den Releasezweig erfordert **separate ausdrückliche menschliche Freigabe** und den [Canonicalizer](../canonicalizer/SKILL.md) mit Feature-Parent/Base/Headprüfung.
7. Kein automatisch anschließendes Release, Mainmerge, Tag, Public Upload, Deployment oder Cleanup.
