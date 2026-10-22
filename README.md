# Agentic Workflow Concept

Projektübergreifendes Konzept für planungsgetriebene, nachvollziehbare und überprüfbare Softwareentwicklung mit spezialisierten KI-Agenten, unabhängigem Review und kontrollierter Git-Übernahme.

**Repository-Zweck:** Erarbeitung eines allgemeinen Vorgehens und eines dazugehörigen einsatzfähigen Anwendungspakets. **Initialer Arbeitsstand:** vollständig ausgearbeitetes Basismodell für einen komplexen, streng abgesicherten Anwendungsfall; noch **nicht** in allen Themen vom Auftraggeber gemeinsam abschließend geprüft oder für produktiven Einsatz freigegeben. Diese Angabe ist Repository-Metadokumentation, nicht Teil der sachlichen Systembeschreibung.

## Drei Ebenen

| Ebene | Aufgabe | Einstieg |
| --- | --- | --- |
| [01_ARBEITSEBENE](01_ARBEITSEBENE/README.md) | Originalquellen, Analysen, offene Fragen, Themenprüfungen, Entscheidungen und Bearbeitungshistorie | [Themenübersicht](01_ARBEITSEBENE/03_THEMENINDEX.md) |
| [02_ALLGEMEINES_KONZEPT](02_ALLGEMEINES_KONZEPT/README.md) | Autoritative, rollenunabhängige Beschreibung des gesamten Systems im jeweils konsolidierten Stand | [Gesamtmodell](02_ALLGEMEINES_KONZEPT/00_GESAMTMODELL.md) |
| [03_ANWENDUNGSEBENE](03_ANWENDUNGSEBENE/README.md) | Abgeleitete, einsetzbare Rollen-Skills, Referenzen, Promptvorlagen, Schemas, Prüfer und Projektstruktur | [Einsatzleitfaden](03_ANWENDUNGSEBENE/README.md) |

**Autorität:** Fachliche Norm liegt ausschließlich in `02_ALLGEMEINES_KONZEPT/`. Die Anwendung operationalisiert sie. Diskussionen, historische Entscheidungen und Unklarheiten stehen ausschließlich auf der Arbeitsebene. Eine Dokumentänderung am Konzept zieht die Prüfung der betroffenen Anwendungsteile nach sich.

## Arbeitsweise dieses Repositories

Wir arbeiten vorerst auf einem separaten Entwicklungsbranch, vorgeschlagen `work/gesamtkonzept-v1`. `main` dient vollständigen, abgestimmten Gesamtfassungen. Dies ist die gegenwärtige Arbeitsorganisation des **Konzept-Repositories**, keine schon verabschiedete universelle Branchpflicht des konzipierten Systems. Initialer Inhaltscommit gehört auf den Entwicklungsbranch; nicht auf `main`.

## Einstieg

1. [Arbeitsgrundlage und Quellenlage](01_ARBEITSEBENE/README.md) sowie [Arbeitsmethode](01_ARBEITSEBENE/01_ARBEITSMETHODE.md) lesen.
2. Fachlich zunächst [Gesamtmodell](02_ALLGEMEINES_KONZEPT/00_GESAMTMODELL.md), dann die thematischen Konzeptkapitel lesen.
3. Operatives Projekt zunächst mit [Einsatzleitfaden](03_ANWENDUNGSEBENE/README.md) und [Projektstruktur](03_ANWENDUNGSEBENE/PROJEKTSTRUKTUR/README.md) vorbereiten.
4. Bei der gemeinsamen Überarbeitung je Thema: Quellen prüfen → Regelung entscheiden → Konzeptebene konsolidieren → Anwendung angleichen → Prüfscripte ausführen.

## Technische Prüfungen (offline, lesend)

```powershell
python 03_ANWENDUNGSEBENE/SKRIPTE/check_repository.py
python -m unittest discover -s tests -v
```

Es werden keine Remote-Operationen, Git-Merges, Deployments, Agentenstarts oder Freigaben durch diese Prüfungen ausgeführt.

## Erster durchgehender Grundstand

Die initiale Konzeptebene ist bereits vollständig ausformuliert (inklusive Planung und Härtung), die operativen Rollen-/Run-/Status-/Feature-/Releasevorlagen sind vorhanden. **Nicht** abgeschlossen ist die gemeinsame themenweise Prüfung und die Produktionsqualifizierung des neuen Frameworks. In der Arbeitsebene steht für jede Regel die Zuordnung zu Anwendungsartefakten und eine offene Besprechungsakte.

## Herkunft und Einschränkung

Das Modell leitet sich aus den vom Auftraggeber übergebenen Notizen, dem Client-V2-Verfahren und der tatsächlichen Arbeit mit Voice-STT-Client-/Server-Projekten ab. Der bekannte gepinnte Referenzstand ist `voice-stt-client`/`feat/client-v2` Commit `b80ed8b81ad92bd02ac32553883443d2b7673bcd`, mit ergänzend geprüften offenen Paket-PRs. Eine historische Quellenkopie ist nicht automatisch die gegenwärtig gültige Projektregel; siehe [Quellenlage](01_ARBEITSEBENE/02_QUELLENUND_HERKUNFT.md). Planung, Planner/Hardener und die allgemeine Feature-/Releasehierarchie beruhen teils auf bisher diskutierten Entwürfen und sind hier erstmals als zusammenhängendes **Initialmodell** formuliert. Die automatische Ausführung durch CLI-Adapter existiert nicht als funktionierendes System und wird nicht behauptet.
