# Begriffe und Invarianten

| Begriff | Verbindliche Bedeutung |
| --- | --- |
| Auftraggeber | Menschliche Instanz, die grundlegende Ziele und ausdrücklich reservierte Freigaben verantwortet |
| Planner | Verantwortlicher Integrator der Gesamtplanung; besitzt innerhalb des genehmigten Planumfangs die alleinige operative fachliche Planpflege |
| Architect | Spezialist für Architektur-/Schnittstellenentwurf und -prüfung; berichtet an Planner, ersetzt dessen Gesamtverantwortung nicht |
| Hardener | Unabhängige, vorzugsweise adversariale Planprüfung; liefert Findings und Beweise, ändert nicht eigenmächtig Plan oder Baseline |
| Planreviewer | Prüft nach der Härtungsdisposition die Vollständigkeit und Freigabereife des konsolidierten Plans unabhängig |
| Orchestrator/Dispatcher | Rekonstruiert den tatsächlich belegten Iststand und bestimmt den nächsten zulässigen Auftrag; seine Entscheidung erteilt keine neuen Rechte |
| Implementer/Corrector | Erstellt und korrigiert einen Kandidaten auf der autorisierten Arbeitslinie; Selbstprüfung, niemals Eigen-ROOT_PASS |
| Technical Reviewer | Fachlich unabhängige Abnahme des vollständigen Kandidaten; dokumentiert Findings oder ROOT_PASS |
| Canonicalizer | Führt ausschließlich gesondert freigegebene, überprüfte kanonische Übernahmen aus |
| Release Qualifier | Qualifiziert den integrierten Release-Candidate einschließlich Provenienz und Pflichtplattformen |
| Owner | Sachlich oder schreibrechtlich verantwortliche Rolle, nicht automatisch Inhaber von Git-Adminrechten |
| DoD | Definition of Done: sämtliche Anforderungen und Nachweise, die vor dem betreffenden Gate vorliegen müssen |
| Provenienz | Nachvollziehbare Zuordnung von Auftrag, Quellstand, Tests, Laufzeit, Review, Freigabe und Git-/Artefaktergebnis |
| Selected Candidate | Der durch belegte Entscheidung ausgewählte, eindeutige weiterzuführende Kandidat |
| ROOT_PASS | Gültiges unabhängiges fachliches Urteil für exakt den geprüften Kandidaten und Umfang; keine Übernahmefreigabe |
| ACCEPTED/CANONICALIZED | Tatsächlich freigegebener und überprüfter Aggregatabschluss auf der kanonischen Ziellinie |
| SUPERSEDED | Nach ausdrücklicher Entscheidung abgelöster Kandidat; historisch nicht gelöscht |
| BLOCKED | Pflichtvoraussetzung fehlt, ist widersprüchlich oder unerreichbar; begründete unbetroffene Teilprüfungen dürfen zulässig bleiben |

## Vier Verbindlichkeitsarten

**V1 – Exakter externer oder interner Vertrag:** Wireprotokolle, Schemas, Identitäten, Kompatibilitätsregeln, Rechte-/Sicherheitsgrenzen. Änderung nur durch geregelte Plan-/Kontraktentscheidung.

**V2 – Funktionale und organisatorische Pflicht:** Produktwirkung, Fehler-/Rückfallverhalten, Abnahme, Mindestnachweis. Erreichtes Ergebnis und Schutzwirkung sind verbindlich; geeignete interne Realisierung bleibt offen.

**V3 – Umsetzungsvorschlag:** Beispielklassen, Dateinamen, Designskizzen, einzelne Ablaufschritte. Zulässige Abweichung mit knapper Begründung, solange V1/V2 eingehalten werden.

**V4 – Technischer Startwert:** Mess-/Tuninginitialisierung ohne fremdverbindliche Wirkung. Mit qualifiziertem Test oder Messung veränderbar; tatsächlich verwendeter Wert ist nachzuweisen.

## Invarianten der Zusammenarbeit

1. **Keine Rechte durch Status:** Templates, Statusfelder, PR-Kommentare und Agentenurteile erteilen keine menschlichen Git- oder Releasefreigaben.
2. **Keine fiktiven Beweise:** `PASS`, `FAIL`, `NOT_RUN`, `NOT_PROVEN`, `SKIPPED_EXPECTED` und begrenzter `PASS_SCOPED` sind getrennte Aussagen.
3. **Keine Selbstabnahme:** Ein fachlicher Beitrag schließt die Unabhängigkeit für dessen technische oder planbezogene Prüfung aus.
4. **Keine stillen Planänderungen:** Auswirkungen auf Verträge, Produktziele, Paketgrenzen und Abnahmebedingungen bedürfen geregelter Disposition.
5. **Keine konkurrierende Schreibhoheit:** Ein freigegebener Candidate-Branch besitzt zu jedem Zeitpunkt einen nachweisbaren Schreibowner; Übergabe ist explizit.
6. **Keine Umschreibung historischer Runs:** Fortsetzungen im offenen Run möglich; neue fachliche Prüfläufe erhalten neue Identitäten.
7. **Keine vorweggenommene Kanonisierung:** Reales Git-/PR-Ergebnis und Baum-/Parentprüfung bestimmen den Abschluss, nicht ein Vorabtext.
