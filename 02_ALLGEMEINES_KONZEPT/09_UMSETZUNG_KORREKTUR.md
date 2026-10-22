# Umsetzung, Selbstprüfung und Korrektur

## Implementierungsauftrag

Der Implementer arbeitet von der gültigen Planbaseline und dem tatsächlichen kanonischen Parent auf dem zugewiesenen Paketbranch beziehungsweise isoliertem Worktree. Er überprüft Vorgänger-PASS, menschliche Übernahme, Git-Aggregation und eigene Berechtigung, bevor er abhängige Änderungen beginnt. Produktziele, Verträge und Schutzwirkungen gelten vollständig; intern darf er eine einfachere oder robustere Implementierung wählen, sofern ihre Gleichwertigkeit nachgewiesen und die betroffenen Schnittstellen dokumentiert werden.

## Selbstdurchlauf

1. Ausgangsbasis, technische Umgebung und reproduzierbare Vorherbedingungen festhalten.
2. Umfang und konkrete Requirements/DoD abarbeiten; unerwartete fachliche Abweichung zum Planner eskalieren.
3. Gezielte Regressionen, Grenz-, Fehler- und Negativtests ausführen; entdeckte Fehler innerhalb des beauftragten Scopes iterativ beheben.
4. Die vollständige betroffene Pflichtregression, Build-/Installations-/Integrations- und reale Plattformfälle gemäß Paket-Testplan ausführen.
5. Ergebnisse an exakte Quell-/Test-/Runtime-/Artefaktidentität binden; vollständige Logs/Exitcodes/Hashes sichern.
6. Traceability, betroffene Produkt-/Planstellen, Status und eigene Runakte konsistent aktualisieren.
7. Mit SHA/Tree, Parent, PR, Report, offenen Grenzen und nächster Aktion als `REVIEW_READY` übergeben und Branchfreeze einhalten.

## Korrekturlauf

Bei `CHANGES_REQUIRED` übernimmt der Implementer die vollständige Reviewspitze als Fast-forward und liest alle maßgeblichen Findings. Der Korrekturlauf umfasst Repro, konkrete Änderung, fokussierte und erforderliche vollständige Requalifikation, neue Runakte und erneute `REVIEW_READY`-Abgabe desselben kumulativen Kandidaten-PRs. Alte Reports bleiben unverändert.

Wird ein Finding fachlich bestritten, weil Repro falsch, Fix unverhältnismäßig oder Architekturfolgen unzulässig sind, erstellt der Implementer einen dokumentierten Gegenbefund. Er verändert die Anforderungen nicht eigenmächtig; Planner beziehungsweise unabhängiger Reviewer entscheidet den fachlich korrekten weiteren Weg. Eine Produktänderung nach PASS hebt dessen Gültigkeit für den neuen Stand auf.
