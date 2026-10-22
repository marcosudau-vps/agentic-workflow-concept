# Akten, Zustandsdarstellungen, Traceability und Evidenz

## Quellen der Wahrheit

- **Statusdatei:** maschinenlesbare aktuelle Übersicht mit ausgewähltem Kandidaten, Phase, Rolle, letzten Belegen, Freigaberef und nächster Aktion; kann gegenüber einer aktiven Arbeitslinie veraltet sein.
- **Paketakte:** Paketumfang, Status, Parent, Branch/PR und vollständiger Runindex; verweist auf die maßgeblichen Originale.
- **Runakte:** ursprünglicher Auftrag, genau ein Bericht mit Resultat/Findings, Evidenzindex und nur benötigte zusätzliche Belege; abgeschlossene Runberichte bleiben historisch fix.
- **Planung:** freigegebene Requirements, Kontrakte, Paketzuordnung und Testdefinitionen sind Norm; tatsächliche Belege füllen erst bei Durchführung den Nachweisteil.
- **Git/PR:** tatsächliche Refs, SHA, Tree, Merge-/Transportergebnis entscheiden die kanonische Geschichte.

## Ablagelogik

Ein Paket enthält `00_PAKET.md`, optional `01_ENTSCHEIDUNGEN.md` und `RUNS/Rnn-<ROLLE>/`. Jeder tatsächliche Run enthält `00_PROMPT_ORIGINAL.md`, `01_REPORT.md` und `EVIDENCE/INDEX.md`. Weitere Dateien entstehen nur bei konkreter Notwendigkeit. Nachsteuerungsprompts einer fortgesetzten Session werden chronologisch als unveränderte Zusatzaufträge archiviert, ohne künstlich einen neuen Run zu starten.

## Provenienzpflicht

Evidenz dokumentiert Erzeuger/Quelle, Befehl oder manuelle Methode, Zeitpunkt, Plattform/Runtime, Exitcode und Ergebnis, relevante SHA/Tree/Build-/Containeridentitäten sowie Checksumme externer Artefakte. Geheimnisse, echte Audioaufnahmen, private Transkripte und Credentials werden nicht offen in Git aufgenommen. Vertrauliche externe Nachweise erhalten einen zulässigen privaten Aufbewahrungsort mit referenzierbarer Identität.

## Statuskonsistenz

Die aktiven Werte von Statusdatei, Paketkopf, Manifest, PR-Zusammenfassung und gültigem Runbericht müssen übereinstimmen. Historische Reports behalten ihre früheren Zustände. Fehlende aktive Statusnachträge dürfen anhand wirklicher Git-/PR-Provenienz aktualisiert werden; fehlende Freigaben oder Tests werden niemals rückwirkend erdichtet.

## Testvokabular

`PASS` bedeutet nachweislich erfüllte Kriterien; `FAIL` tatsächliches Scheitern; `NOT_RUN` nicht durchgeführt; `NOT_PROVEN` durchgeführt, aber Wirkung/Identität nicht ausreichend belegt; `SKIPPED_EXPECTED` ausdrücklich zugelassener Ausnahmefall; `PASS_SCOPED` nur für genau umrissenen Teil. Ein Defekt, der eine andere Testgruppe blockiert, kann zulässige unbetroffene Teiltests erlauben – die globale Abnahme bleibt entsprechend offen.
