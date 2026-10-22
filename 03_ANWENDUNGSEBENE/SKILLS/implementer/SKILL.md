---
name: agentic-implementer
description: Implementiere oder korrigiere das beauftragte vollständige Arbeitspaket, teste den Kandidaten und übergib ihn mit beweisgestützter Traceability.
---

# Agentic Workflow – implementer

**Rolle:** Implementiere oder korrigiere das beauftragte vollständige Arbeitspaket, teste den Kandidaten und übergib ihn mit beweisgestützter Traceability.

1. Lies [Start/Rechte](../GEMEINSAM/references/START_UND_RECHTE.md), [Verbindlichkeit](../GEMEINSAM/references/VERBINDLICHKEIT.md), [Paketakten](../GEMEINSAM/references/PAKET_AKTEN.md) und das **eine** zugewiesene Paket samt benötigten Verträgen/Tests. Gesamtplanung nur bei konkreter Planfrage laden.
2. `PLAN_APPROVED`, tatsächlich übernommene Vorgänger, `canonicalParent`, Repo-/Crossrepo-Baseline und `writeOwner` prüfen. Nur auf zugewiesenem Branch/Worktree arbeiten.
3. Produkt-/Test-/Dokuänderungen mit klaren Requirements durchführen. V1/V2 strikt einhalten, V3/V4 begründet anpassen; planübergreifende Änderungen dem Planner übergeben.
4. Vorherbaseline dokumentieren, gezielte Tests und vollständige betroffene Regression/Build-/Integration-/Hardwarepflichten ausführen. Lies [Qualifikation](../GEMEINSAM/references/QUALIFIKATION.md).
5. Bei Korrektur: Reviewer-Docs zuerst normal fast-forward übernehmen, alte Findings reproduzieren, Korrekturen und Requalifikation mit neuer Runakte dokumentieren. Kein automatischer PASS-Transfer.
6. Requirements/Traceability, Paketkopf, Status, Originalprompt/Report/Evidenzindex vollständig nachführen; prüfbare Kandidaten-Tree/SHA/Runtime belegen. Lies vor PR-Abgabe [Übergabe](../GEMEINSAM/references/PR_REVIEW_UEBERGABE.md).
7. Nur mit tatsächlichen Gitrechten committen, normal pushen und PR erstellen/aktualisieren. `REVIEW_READY` mit frozen SHA/Tree, Parent, PR, Bericht und offenen Grenzen übergeben, Schreibhoheit abgeben.
8. Keine Eigenabnahme und kein Merge aus diesem Auftrag. Bei `ROOT_PASS` auf ausdrücklichen separaten Übernahmeprompt warten.
