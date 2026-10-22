# Bibliothek operativer Datei- und Aktenvorlagen

Alle Dateien im Unterbaum sind **Musterdateien** mit projektneutralen IDs oder leeren Ergebnissen; sie sind keine tatsächlichen Freigaben, Prüfberichte oder Laufzeitergebnisse. Projektspezifische Daten und tatsächliche Originalaufträge entstehen erst im Zielprojekt. Vorlagen für noch nicht stattgefundene Runs dürfen nicht so importiert werden, als wären sie bereits erfolgt.

- `TRACKING/`: maschinenlesbarer Workflowstatus sowie aktueller Status, Featurestatus und chronologischer Verlauf
- `PLANUNG/`: Planindex, Zielbild, IST, Architektur, Risiken/Entscheidungen, Kontrakte, Requirements/Traceability, Teststrategie, Package-/Featuredefinition und Planstatus
- `PLANUNG/RUNS/`: Muster für Planer/Härtung/Planreview einschließlich Finding/Dispositionsakten
- `AUSFUEHRUNG/`: Paketkopf, optionales Entscheidungsdokument, echte Runartefakte
- `RELEASE/`: Releaseumfang, RC-Matrix und Qualifikations-/Freigabeakt

Die zugehörigen JSON-Schemas stehen unter [SCHEMAS](../SCHEMAS/README.md).
