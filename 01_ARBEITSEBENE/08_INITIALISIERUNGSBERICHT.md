# Initialgrundstand – Quellenumfang, Abdeckung und Übergabe

**Arbeitsstand:** erste vollständig ausgearbeitete Version, nicht themenweise verabschiedet.  
**Zielrepository:** `agentic-workflow-concept`  
**Arbeitsbranch:** `work/gesamtkonzept-v1`, `main` für später komplett geprüfte Gesamtfassungen.

## Eingangsgrundlagen

- 40 archivierte Dateien aus den beiden Ideenentwürfen und historischen Client-V2-Skill-/Governance-Snapshots, byteweise unverändert mit SHA256 in `07_QUELLENMANIFEST.json`.
- Geprüfter Live-Referenzcommit Client-V2 `b80ed8b81ad92bd02ac32553883443d2b7673bcd`. Neue Unterlagen basieren auf bewährten Mechanismen der tatsächlichen Rollen-/Zustands-/Runpraxis und ergänzen eine erst skizzierte Planphase.
- Die historische Quellkopie enthält **nicht sämtliche** Live-Archivalien, Quellcodes und kompletten produktbezogenen Runs. Das vermeidet die Mitnahme konkreter Projektdaten in ein allgemein nutzbares Konzept-Repository.

## Abdeckung

- 16 thematische neutrale Konzeptkapitel plus allgemeines Systemmodell (17 Dateien).
- 10 zielgerichtete Rollen-Skills, gemeinsame Referenzen, 16 Promptvorlagen, Status-/Plan-/Feature-/AP-/Run-/RC-Vorlagen, JSON-Schemas und Python-Checks.
- 19 themenbezogene Arbeitseinträge mit Konzept-/Anwendungspfad und noch ausstehendem Einzelentscheid.

## Grenzen der Erstfassung

Die Plan-/Feature-/Releasehierarchie ist eine bewusst konkrete Operationalisierung bisheriger Ideen. Sie wurde noch nicht unabhängig als Framework produktiv betrieben. Die Skripte prüfen Struktur, nicht die fachliche Wahrheit oder GitHub-Berechtigungen. Der Dispatcher ist zunächst ein Rollen-Skill, kein laufender Dienst. Große, speziell projektspezifische Testharnesses und Produktionsadapter gehören nicht in den generischen Kern.

## Veröffentlichungsschutz

Vor einem öffentlichen GitHub-Push die archivierten, teilweise projektspezifischen historischen Quellen auf vertrauliche Inhalte, personenbezogene Daten, interne Pfade und Secrets prüfen. Eine automatische Datenschutzfreigabe ist mit dieser Grundfassung **nicht** verbunden. Das Konzept selbst und die neutralisierten Einsatzvorlagen sind nicht von den historischen Rohquellen abhängig.
