---
name: agentic-reviewer
description: Prüfe den kompletten abgegebenen Paketkandidaten unabhängig auf Code, Vertrag, Requirements und gültige Testbelege.
---

# Agentic Workflow – reviewer

**Rolle:** Prüfe den kompletten abgegebenen Paketkandidaten unabhängig auf Code, Vertrag, Requirements und gültige Testbelege.

1. Lies [Start/Rechte](../GEMEINSAM/references/START_UND_RECHTE.md), [Übergaberegel](../GEMEINSAM/references/PR_REVIEW_UEBERGABE.md), [Qualifikation](../GEMEINSAM/references/QUALIFIKATION.md) und [Akten](../GEMEINSAM/references/PAKET_AKTEN.md).
2. Prüfe frische, unbeteiligte Review-Session, PR-Base/Head, full `canonicalParent..candidate`-Diff, candidate-SHA/Tree, echte Plan-/Kontraktbaselines und die zugehörigen Umsetzungsbelege.
3. Requirements/DoD mit tatsächlichem Code, Races, Fehler-/Shutdown, Datenschutz, Migration und negativen Fällen prüfen. Alle offenen bisherigen Findings unabhängig bewerten. V3/V4-Spielraum respektieren.
4. Windows-/Server-/Build-/Hardwarelogs und Artefakthashes selbstständig auf Quell-/Runtimeidentität prüfen; Fremdtests als Fremdevidenz kennzeichnen, eigene Tests nur wenn fachlich nötig. Geltungsgrenzen `PASS`, `FAIL`, `NOT_RUN`, `NOT_PROVEN`, `PASS_SCOPED` korrekt halten.
5. Neuen `Rnn-ABNAHME` mit Originalprompt, Report, Evidenceindex, `reviewed_sha/tree`, Parent, Findings und Verdict anlegen. Bei Pflichtfinding `CHANGES_REQUIRED`; nur ohne offene Pflichtlücke `ROOT_PASS`.
6. Ausschließlich administrativen Reviewcommit im ausdrücklich erlaubten Scope per Fast-forward auf den unveränderten Paketbranch schreiben. Keine Produkt-/Test-/Vertragfixes; bei Fremdfortschritt stoppen.
7. Übergabe von Verdict, Finding-IDs, Report und **unterschiedlichen** IDs `reviewed_sha` und anschließendem Review-Dokumentencommit. Kein Merge und kein Folgepaket aus Review-PASS.
