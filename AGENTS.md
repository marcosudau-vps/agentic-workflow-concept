# Agent-Regeln – Arbeit am Repository `agentic-workflow-concept`

Diese Anweisung betrifft **die gemeinsame Bearbeitung dieses Konzept-Repositories**; sie ist nicht mit den Rollenregeln gleichzusetzen, die das hier spezifizierte System später in andere Projekt-Repositories ausrollt.

## Geltung und Autorität

- Die inhaltliche Gesamtdefinition befindet sich in `02_ALLGEMEINES_KONZEPT/` und ist vollständig, sachlich, rollenunabhängig, ohne historische Diskussionen, Entscheidungserklärungen, offene Fragen oder Änderungsgeschichten zu halten.
- Entscheidungen, Quellen, Varianten, Historie, Ungeklärtes und Besprechungsprotokolle gehören ausschließlich nach `01_ARBEITSEBENE/`.
- `03_ANWENDUNGSEBENE/` operationalisiert die fachliche Beschreibung in Rollen-Skills, Lesepfaden, Vorlagen, Schemata und Tools; dort dürfen keine abweichenden fachlichen Regeln heimlich entstehen.
- Der Initialgrundstand ist **noch nicht gemeinsam thematisch bestätigt**; er ist eine konsistente Arbeitsbasis, nicht das fertige endgültige Framework.

## Wenn du ein Konzeptthema bearbeitest

1. Lies `README.md`, `01_ARBEITSEBENE/01_ARBEITSMETHODE.md` und die zum Thema passende Akte aus `01_ARBEITSEBENE/THEMEN/`.
2. Ermittle die zur Frage gehörenden neutralen Konzeptkapitel und ihre Einträge in `06_ABLEITUNGSMATRIX.csv`. Historische Quellen in `01_ARBEITSEBENE/QUELLEN/` sind Belegmaterial; sie dürfen nie ungeprüft aktuelle Projektregeln überschreiben.
3. Besprich inhaltliche Änderungen mit dem Auftraggeber. Keine eigenmächtige Grundsatzfestlegung bei unterschiedlichen plausiblen Optionen.
4. Dokumentiere tatsächliche Entscheidung und Begründung nur in der Arbeitsebene; führe das **gesamte** betroffene Konzept sachlich und widerspruchsfrei nach, ohne dort Änderungsprotokolle zu schreiben.
5. Aktualisiere die betroffenen Rollen-/Vorlagen-/Skripte-/Schemadateien in `03_ANWENDUNGSEBENE/`; prüfe die Ableitungsmatrix.
6. Führe `python 03_ANWENDUNGSEBENE/SKRIPTE/check_repository.py` und `python -m unittest discover -s tests -v` aus; melde Prüfung/fehlende fachliche Punkte.

## Git- und Scopegrenzen

- Unsere **aktuelle** Arbeitsorganisation: Entwicklungsbranch `work/gesamtkonzept-v1`, Main erst für die gemeinsam freigegebene, vollständige Gesamtfassung. Das ist noch keine verbindliche universelle Branchregel des Systems.
- Kein Push/Merge, keine Veröffentlichung/Tags, kein Deployment und kein Löschen ohne dafür tatsächlich erteilten Auftrag. Fremde lokale WIP erhalten; keine Force-Pushes.
- Der finale Übergang nach `main` erfolgt erst nach tatsächlicher gemeinsamer Gesamtprüfung und ausdrücklicher Freigabe.

## Sicherheit

Keine Secrets, Tokens, private Nutzerdaten oder reale Audiodaten in Git. Vor Übernahme historischer Quellen in ein öffentliches Repository deren Inhalt/Vertraulichkeit prüfen. Eine erfolgreiche Struktursuite ist kein fachlicher Gesamt-PASS.
