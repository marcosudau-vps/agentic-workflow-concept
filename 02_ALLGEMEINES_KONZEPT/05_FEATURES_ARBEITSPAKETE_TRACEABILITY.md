# Features, Arbeitspakete, Anforderungen und Traceability

## Feature

Ein Feature ist eine kohärente, benutzer- oder systemseitig sinnvolle Veränderung mit eigenem Zielzustand, Abnahme, Dokumentation und Integrationsverantwortung. Sein Umfang kann aus einem kleinen Arbeitspaket oder einer umfangreichen, verschachtelten Arbeitspakethierarchie bestehen. Innerhalb eines Features kann der Planner mehrere seriell oder nach explizit nachgewiesenen Entkopplungsgrenzen parallel bearbeitbare Aufgaben zuschneiden.

## Arbeitspaket

Ein Arbeitspaket wird so geschnitten, dass ein umsetzender Agent eine vollständig überprüfbare Ergebniseinheit liefern kann. Verbindliche Mindestinformationen: `id`, Ziel, Scope/Nichtziele, Requirements, Quellbaseline, technische Verträge, Abhängigkeiten, vorgeschlagene Umsetzung, erlaubte Freiheiten, Pflichtnachweise, Abnahmekriterien, DoD, verantwortliche Rolle, erwartete Git-/Run-/Evidenzpfade und Übergabeschnittstellen.

Arbeitspaketgrenzen dürfen notwendige und begründete Integration gemeinsamer Dateien nicht verhindern, aber keine unautorisierten Folgefeatures verbergen. Änderungen des Requirement-Owners oder übergreifender Vertragsgrenzen benötigen Planentscheidung.

## Eindeutige Traceability

Jede verbindliche Anforderung erhält eine stabile ID mit fachlich überprüfbarer Wirkung. Die Kette ist:

`Ziel → Requirement-ID → Kontrakt/Designanker → Feature/AP-Owner → Testfall/Methode → Kandidat-SHA/Tree/Runtime → Evidenz/Run → unabhängiges Urteil → Aggregat/Release`.

Requirements-JSON ist die strukturierte Hauptdarstellung; menschenlesbare Tabellen und Paketübersichten sind davon abgeleitete oder konsistent zu haltende Ansichten. `NOT_RUN` wird nicht als `PASS` gewertet. Ein Testname oder eine geplante Testdatei ohne ausführbare Prüfung ist kein Erfolgsnachweis.

## Parallelität

Parallel ausführbare Aufgaben haben vorher festgelegte unveränderliche Vertragsbaselines, eindeutige Schreib-/Ownergrenzen und eine Integrationsreihenfolge. Derselbe Kandidatenbranch besitzt niemals zwei konkurrierende Schreibowner. Ergebnisse werden gegen einen identifizierten Integrationsparent geprüft; veraltete Basen werden nicht durch stillen Rebase oder beliebige Mergeentscheidung angenommen. Der tatsächliche Integrationsabschluss bleibt serialisiert.

## Paketabschluss

Jedes auf einer kanonischen Integrationslinie angenommene Arbeitspaket wird dort als genau ein nachvollziehbarer Single-Parent-Aggregatcommit repräsentiert, sofern die geplante Featurehierarchie diese Paketlinie als Integrationsschicht definiert. Ursprüngliche Reviews, Korrekturen, Tests und Prompt-/Runakten sind Bestandteil oder eindeutig verlinkte Provenienz des Ergebnisses.

## Featuregesamt-Gate

Die vollständige Featuregesamtfassung durchläuft nach kanonischer Aufnahme ihrer Arbeitspakete eine **unabhängige Integrations- und Featureprüfung**. Diese bewertet die gesamte Funktionseinheit einschließlich Crosspaket-Beziehungen, Build-/Runtime-/Migrationsnachweisen und Dokumentation. Ein unabhängiges `FEATURE_ROOT_PASS` führt nur zum Warten auf ausdrückliche menschliche Freigabe. Erst eine separat autorisierte und real geprüfte Single-Parent-Aggregation im Releasezweig schließt das Feature ab.
