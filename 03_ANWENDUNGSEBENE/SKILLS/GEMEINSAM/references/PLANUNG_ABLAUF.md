# Planung – operative Durchführung

## Plannerstart

- Ursprünglichen Auftrag und Planungsrechte sichern, Istzustand (Repo/Code/Vertrag/Betrieb) dokumentieren.
- Zielbild, Nichtziele und Akzeptanz nachfragen oder aus belegten Quellen auflösen; nicht erraten.
- Architektur-/Kontraktgrundlagen gemeinsam aus einer Sicht integrieren; ggf. Architect mit gezieltem Auftrag und nur relevanter Baseline einsetzen.
- Requirements stabil ID-basiert in JSON mit Test-/Owner-/Vertragsanker pflegen; Paketmanifest und Abhängigkeiten ableiten.
- Detaillierte Test-/Integrationsstrategie, Plattformmatrix, Crossrepo-Bindungen und Übergaben vorbereiten.
- Jede Datei im Planindex mit Versions-/Hash-/Quellbezug aufführen; falsche Selbst-SHA im noch nicht committeten Inhalt vermeiden.

## Hardening

- Genau definierten Plan-SHA/Tree oder Snapshot für den unabhängigen Hardener einfrieren.
- Schwerpunkt je Lauf festlegen: Architektur, Races, Protokoll, Sicherheit, Traceability, Prompt-Ambiguität oder adversariale Gegenbeispiele.
- Hardener berichtet Findings; Planner entscheidet über Disposition; keine stillen Mutationen auf Hardenerzweig.
- Jeden akzeptierten Planfix auf alle betroffenen Verträge, Requirements, Testfälle, APs und Vorlagen übertragen.
- Endreview in frischer unabhängiger Session für den vollständig konsolidierten Plan.

## Planfreigabe

`PLAN_ROOT_PASS` → Mensch prüft und genehmigt Planfreeze → `PLAN_APPROVED` mit konkretem Baseline-SHA/Tree, tatsächlichem Originalprompt und Planindex. Keine abhängige Paketumsetzung vor dem tatsächlichen Gate. Änderungen an V1/V2 während Ausführung zurück in Planänderungsprozess, mit gezielter erneuter Qualifikation.
