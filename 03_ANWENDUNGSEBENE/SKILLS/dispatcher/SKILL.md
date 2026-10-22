---
name: agentic-dispatcher
description: Ermittle aus Git, PRs, Plan-/Paketakten und Freigaben genau einen nächsten zulässigen Schritt; führe keine Rechte- oder Rollenerfindung durch.
---

# Agentic Workflow – dispatcher

**Rolle:** Ermittle aus Git, PRs, Plan-/Paketakten und Freigaben genau einen nächsten zulässigen Schritt; führe keine Rechte- oder Rollenerfindung durch.

1. Lies [Status- und Gatevertrag](../GEMEINSAM/references/STATUS_UND_GATEPRUEFUNG.md) und [Start/Rechte](../GEMEINSAM/references/START_UND_RECHTE.md).
2. Lies gültige projektbezogene AGENTS und aktuelle Steuerungsindizes. Suche **zuerst offene Paket-/Feature-PRs** und deren Head-Status, nicht nur die abgeschlossene Integrationslinie.
3. Identifiziere genau einen ausgewählten Kandidaten und den dazugehörigen tatsächlichen Run-/Writeowner. Prüfe Git-/Review-/Freigabeprovenienz.
4. Erkenne die Phase und den nächsten erlaubten fachlichen Schritt. Bei aktiver fremder Session, ungeklärten Rechten oder konfligierender Auswahl keine freie Fortsetzung.
5. Melde kurz: Phase, Scope, Projekt/AP/Feature, SHA/Tree/Parent, Owner, gewählte Rolle, Quellen und Blocker. Übernimm danach nur die eine tatsächlich beauftragte fachliche Aktion nach dem passenden Skill.
6. Eigenreview oder Übergang zum Folgepaket aus demselben Auftrag ist nicht erlaubt; `ROOT_PASS` ohne menschliche Freigabe wartet.

**Routing:** Planung → [planner](../planner/SKILL.md), Härtung → [hardener](../hardener/SKILL.md), Planreview → [plan-reviewer](../plan-reviewer/SKILL.md), Umsetzung/Korrektur → [implementer](../implementer/SKILL.md), technische Abnahme → [reviewer](../reviewer/SKILL.md), autorisierte Übernahme → [canonicalizer](../canonicalizer/SKILL.md), Featuregesamtprüfung → [feature-qualifier](../feature-qualifier/SKILL.md), Releaseprüfung → [release-qualifier](../release-qualifier/SKILL.md).
