# Paket-PR und unabhängige Schreibübergabe

1. Kandidat vom letzten echten kanonischen Parent; kumulativer Paketbranch mit genau einem PR zum vorgesehenen Integrationszweig.
2. Vor `REVIEW_READY`: vollständiger Kandidat inkl. Runbericht/Logs/Test-IDs/Traceability, sauberer Workingtree, verifizierbarer SHA/Tree und PR-Head. Umsetzer pausiert Pushes.
3. Reviewer prüft exakten eingefrorenen SHA und vollständigen `parent..candidate`-Diff, nicht eine abgeschnittene Webansicht.
4. Reviewer commitet/pusht nur nach expliziter Gitfreigabe administrative Run-/Review-/Statusakten per normalem Fast-forward auf den **gleichen** Paketbranch; kein eigener Produktfix und kein zweiter Review-PR. Bei Fremdfortschritt stoppen.
5. Report enthält `reviewed_sha/tree` vor dem eigenen Docs-Commit; Gitidentität der neuen Reviewspitze nach Erstellung in Übergabe ermitteln.
6. Bei Findings holt Implementer die Reviewsparte vor der Korrektur fast-forward. Danach alle betroffenen Volltests wiederholen und frischen unabhängigen Review starten.
7. Bei PASS bleibt `ROOT_PASS/WAITING_FOR_APPROVAL`, bis ein menschlicher Abschlussauftrag vorliegt.
8. Vor Merge `reviewed_sha → final-head` auf ausschließlich genehmigte Docs-/Freigabeänderungen und finale Head-CI prüfen.

Keine Mergefreigabe aus einem technischen PASS oder einem Statusfeld ableiten. Keine stillen Force-Pushes, Historymerges oder Rebases.
