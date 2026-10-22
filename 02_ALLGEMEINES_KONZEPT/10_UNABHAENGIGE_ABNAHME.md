# Unabhängige technische Abnahme

## Prüfidentität und Gegenstand

Die unabhängige Session verifiziert Repository, Base, Candidate-SHA/Tree, Parent, relevante andere Repository-/Runtime-SHAs, eingefrorenen Prüfgegenstand, vollständige Diffoberfläche und zugehörige Nachweise. Sie prüft das **gesamte Paket gegen die fachliche Baseline**, nicht lediglich den letzten Korrekturcommit oder PR-Kurztext.

## Prüfung

- Requirements, Akzeptanzkriterien und verbindliche Kontrakte fallgenau mit Code und Tests abgleichen.
- Negative, Race-, Recovery-, Datenmigration-, Sicherheits- und Shutdownpfade soweit betroffen prüfen.
- Vollständige Pflichtregressions- und Buildsuiten aus den tatsächlichen Umsetzungsbelegen mit Befehl, Runtime, Ergebnis und SHA/Tree auf Gültigkeit kontrollieren.
- Reale Test-/Hardwarebelege auf Herkunft und Wirkung bewerten. Der Reviewer führt die komplette Umgebungssuite nicht allein zur Redundanz erneut aus; er fordert gezielte Repros bei konkreten Risiken und Lücken.
- Die Konsistenz von Runakten, Traceability, Status, PR und Gitidentität beurteilen.

## Verdict und Finding

`ROOT_PASS` setzt sämtliche dem Paket zugehörigen Pflichtkriterien sowie alle früheren offenen Pflichtfindings in nachweisbar geschlossenem Zustand voraus. `CHANGES_REQUIRED` enthält reproduzierbare, priorisierte Findings mit Requirementbezug, Beleg, Expected/Actual, Owner und verlangtem Nachweis. `BLOCKED` benennt exakt den fehlenden Zugriff oder die unbelegte Voraussetzung. Ein `PASS_SCOPED` für einzelne Testbereiche erzeugt keinen Gesamt-PASS.

Der Reviewer schreibt keine fachlichen Produkt-, Test-, Kontrakt- oder Planänderungen. Sein eigener administrativer Dokumentcommit ist von der fachlich geprüften SHA zu unterscheiden; eine spätere Kanonisierung prüft den kompletten diff `reviewed_sha → finaler Head` auf ausschließlich autorisierte administrative Änderungen. Eine neue fachliche Änderung erfordert erneute unabhängige fachliche Abnahme.

## Abschluss

Ein gültiger `ROOT_PASS` führt nur zu `WAITING_FOR_APPROVAL`. Die menschliche Übernahmeentscheidung und Git-Kanonisierung sind separate Gates. Ein ausdrückliches zusätzliches unabhängiges Review erzeugt einen neuen Run; frühere offene Pflichtbefunde bleiben bis zur nachgewiesenen Schließung wirksam.
