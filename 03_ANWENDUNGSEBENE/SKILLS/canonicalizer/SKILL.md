---
name: agentic-canonicalizer
description: Führe ausschließlich nach ausdrücklicher menschlicher Freigabe einen geprüften Aggregatecommit aus und belege Parent-/Treegleichheit.
---

# Agentic Workflow – canonicalizer

**Rolle:** Führe ausschließlich nach ausdrücklicher menschlicher Freigabe einen geprüften Aggregatecommit aus und belege Parent-/Treegleichheit.

1. Lies [Start/Rechte](../GEMEINSAM/references/START_UND_RECHTE.md) und [Übernahme](../GEMEINSAM/references/UEBERNAHME.md), mit PR- und [Reviewübergabe](../GEMEINSAM/references/PR_REVIEW_UEBERGABE.md).
2. Prüfe **Originalprompt der menschlichen Übernahmefreigabe** samt konkretem Paket/Feature/PR, freigegebenem Head, Parent und unabhängigem gültigem PASS. Fehlende Freigabe ist Stop.
3. Prüfe PR-Base/current HEAD, Tree, Reviewer-SHA/Tree, administrativen Diff seit Pass, Mergeability, Pflichtchecks/CI und ausgewählte Integrationslinie direkt vor Aktion.
4. Sichere Freigabeoriginal im ausdrücklich autorisierten administrativen Scope; danach erneut finale Head-/CI-Gültigkeit prüfen.
5. Genau einen autorisierten Squash-/Single-Parent-Aggregatweg durchführen, ohne Force-Push oder Alternativmerge.
6. Nach der tatsächlichen Aktion aus Git/PR Parentanzahl==1, erwarteten Parent, Commitanzahl==1 und Treegleichheit mit letztem autorisiertem Kandidaten prüfen. Fehlversuche nicht als angenommen melden.
7. Melde Abschluss-SHA/Tree, Originalprompt, PASS-Bericht, Git-/CI-Belege und nächste erlaubte Phase. Keine impliziten Releases, Tags, Deployments oder Cleanup.
