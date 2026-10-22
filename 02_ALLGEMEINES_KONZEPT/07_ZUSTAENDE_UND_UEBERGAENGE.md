# Zustandsmodell und zulässige Übergänge

## Planung

| Zustand | Bedeutung | Folgezustand/Gate |
| --- | --- | --- |
| `PLANNING_IN_PROGRESS` | Planner erstellt konsolidierten Entwurf | `PLAN_REVIEW_READY` |
| `PLAN_HARDENING` | Unabhängige Hardener prüfen eingefrorene Prüfidentität | `PLAN_CHANGES_REQUIRED` oder `PLAN_REVIEW_READY` |
| `PLAN_CHANGES_REQUIRED` | Pflichtbefund/Planlücke fordert Plannerdisposition | `PLANNING_IN_PROGRESS` |
| `PLAN_REVIEW_READY` | Konsolidierter Plan und Findings zur unabhängigen Abnahme | `PLAN_ROOT_PASS` oder `PLAN_CHANGES_REQUIRED` |
| `PLAN_ROOT_PASS` | Technischer Planreview für exakten Plan-SHA bestanden | `PLAN_WAITING_FOR_APPROVAL` |
| `PLAN_WAITING_FOR_APPROVAL` | Menschlicher Planfreeze fehlt | `PLAN_APPROVED` |
| `PLAN_APPROVED` | Autorisierte Planungsbaseline vorhanden | Paketausführung zulässig |

## Ausführung und Pakete

| `workflowPhase` | Voraussetzungen | Genau nächste Fachaktion |
| --- | --- | --- |
| `READY_FOR_IMPLEMENTATION` | Freigegebener Plan; alle echten Vorgänger abgeschlossen | Implementer startet ausgewähltes Paket |
| `IMPLEMENTATION_IN_PROGRESS` | Aktiver Run/Schreibowner | Fortsetzen nur durch Owner oder per belegter Recovery |
| `REVIEW_READY` | Vollständiger eingefrorener Kandidat mit Selbstnachweisen | Frische unabhängige Abnahme |
| `REVIEW_IN_PROGRESS` | Reviewowner hält temporäre Schreibhoheit | Review beenden oder geregelte Übergabe |
| `CHANGES_REQUIRED` | Unabhängige Pflichtfindings | Korrektur des gewählten Kandidaten |
| `CORRECTION_IN_PROGRESS` | Beauftragte Korrektur läuft | Same Owner/Recovery |
| `WAITING_FOR_APPROVAL` | ROOT_PASS belegt, keine offenen Pflichtbefunde | Ausdrückliche menschliche Übernahmefreigabe |
| `READY_FOR_CANONICALIZATION` | Passende Freigabe und gültige Identitäten | Ein überprüfter Aggregationsschritt |
| `CANONICALIZED` | Tatsächlicher verifizierter Integrationscommit | Nächstes zulässiges Paket bzw. Featuregate |
| `BLOCKED` | Pflichtvoraussetzung fehlt/konfligiert | Owner/Defekt/Entscheidung konkret klären |
| `SERVER_FIX_REQUIRED` | Crossrepo-Defekt blockiert qualifikationsrelevanten Umfang | Beauftragte Fix-Linie verfolgen |
| `SUPERSEDED` | Kandidat ausdrücklich abgelöst | Historisch sichern, nicht auswählen |
| `COMPLETED` | Alle für den Scope relevanten Gates/Übernahmen nachgewiesen | Feature-/Releaseabschluss |

`packageStatus` (z. B. `ROOT_PASS`, `BLOCKED`) und `workflowPhase` sind unterschiedliche Dimensionen. Ein blockiertes Gesamtpaket kann im bereits autorisierten Scope weiterhin beweisbare Teilprüfungen durchführen; dies darf keine unerfüllten Pflichtgates kaschieren.


## Featuregesamtstatus

Die Paketstatusmaschine ist von der abschließenden Featureprüfung getrennt: `FEATURE_IN_PROGRESS` (laufende Paketaggregate) → `FEATURE_REVIEW_READY` (vollständiger Feature-HEAD mit sämtlichen Paketgates) → `FEATURE_REVIEW_IN_PROGRESS` → bei Finding `FEATURE_CHANGES_REQUIRED`, andernfalls `FEATURE_WAITING_FOR_APPROVAL` mit unabhängiger `FEATURE_ROOT_PASS`-Evidenz. Nach tatsächlichem menschlichem Freigabeoriginal folgt `FEATURE_READY_FOR_CANONICALIZATION`. Erst der nachgewiesene Feature-Aggregatcommit im Releasezweig erzeugt `FEATURE_CANONICALIZED`. `FEATURE_BLOCKED` benennt fehlende Paket-/Integrations-/Freigabebelege.

Ein technischer Paket-PASS ersetzt die Featuregesamtprüfung nicht.

## Zustandsbelege und Dispatcher

Die Zustandsdatei ist eine **Übersicht**, niemals alleiniger Entscheidungsbeweis. Vor der Aktionswahl werden aktuelle offene PRs, Remoteheads, ausgewählte Kandidaten, Schreibowner, Paketakten, Reviewverdicts, Freigaben und Integrationscommits gegengeprüft. Die kanonische Linie kann absichtlich hinter der laufenden Paketlinie zurückliegen. Aus veralteten Statuskopien folgt kein neuer Start.

Mehrere ausgewählte Kandidaten ohne Auswahlbeleg, abweichende SHAs, fremde aktive Schreibhoheit oder fehlende Freigaben führen zu `BLOCKED` beziehungsweise ausdrücklicher Klärung statt freier Aktionswahl. Eine Dispatch-Anfrage darf genau eine fachliche Aktion auslösen, kein unkontrolliertes Durchlaufen sämtlicher Folgegates.
