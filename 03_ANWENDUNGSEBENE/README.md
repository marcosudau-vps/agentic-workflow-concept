# Anwendungsebene – operative Umsetzung des Konzepts

Dieser Bereich enthält **projektneutrale** Rollenverträge, konkrete Lesepfade, Arbeitsschemata, Vorlagen und lokal ausführbare Hilfswerkzeuge. Er ist aus dem allgemeinen Konzept abgeleitet und besitzt **keine konkurrierende fachliche Autorität**.

## Inhalte

- [SKILLS](SKILLS/README.md): Dispatcher, Planner, Architect, Planhardener, Planreviewer, Implementer, Reviewer, Canonicalizer, Featurequalifier, Releasequalifier
- [SKILLS/GEMEINSAM/references](SKILLS/GEMEINSAM/references/README.md): nur bei konkreter Rolle/Phase erforderliche vertiefende Referenzen
- [PROMPTS](PROMPTS/README.md): kurze, auf Parameter und Rollen-Skills gestützte Beauftragungsmuster
- [SCHEMAS](SCHEMAS/README.md): maschinenlesbare JSON-Schemas
- [VORLAGEN](VORLAGEN/README.md): Dateien, die bei Projektstart beziehungsweise erst während Runs entstehen
- [PROJEKTSTRUKTUR](PROJEKTSTRUKTUR/README.md): Ablage-/Deployschema mit korrekter Relativpfadkonvention
- [SKRIPTE](SKRIPTE/README.md): read-only Strukturaudit, Promptgenerierung ohne Fremd-APIs

## Einsatzgrenze

Das Anwendungspaket implementiert die organisatorischen Anweisungen und die **offline prüfbaren Strukturteile**. Es startet keine Agentensessions, führt keine Git-Merges aus und erzwingt keinen plattformseitigen Branchschutz. Solche Aktionen erfordern echte Integrationen und ausdrücklich erteilte Rechte. Eine Vorlage erzeugt niemals eine Freigabe.

## Empfohlener Ablauf im Zielprojekt

1. `PROJEKTSTRUKTUR` einrichten und Vorlagen mit tatsächlicher Projektidentität befüllen.
2. Auftraggeber erteilt Projekt-/Planungsauftrag; Planner dokumentiert Ursprung und Planbaseline.
3. Die Rollen werden über `SKILLS/dispatcher/SKILL.md` beziehungsweise ihre explizite Rolle beauftragt. Der Agent liest nur den relevanten Skill und die von diesem genannten Referenzen.
4. Echte Runs erzeugen fortlaufende Akten; keine leeren Freigabe- und Korrekturakten vorab erstellen.
5. Vor Übergaben Struktur-/Statusprüfung ausführen und fehlende fachliche Pflichtnachweise getrennt prüfen.

Der strenge Grundmodus sieht umfassende Planung, unabhängiges Hardening, Planreview, menschliche Planfreigabe, Paketimplementation, unabhängigen technischen Review, menschliche kanonische Freigaben und Releasequalifikation vor.
