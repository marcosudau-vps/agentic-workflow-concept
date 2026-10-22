# Finding-Vertrag: unabhängige Planhärtung

## Runstart

Originalauftrag, genauer Plan-Commit/Tree, relevante Quellen, gewähltes Prüffeld und ausdrückliche Unabhängigkeit festhalten. Hardener liest Planindex, betroffene Verträge/Architektur/Requirements/APs, dann nur die für die Hypothese nötige ergänzende Evidenz.

## Report

Jedes Finding führt `findingId`, `severity`, `status=OPEN`, `invariant`, `affectedIds`, `scenario`, `expected`, `observed_or_reasoned`, `sources`, `reproduction_or_counterexample`, `impact`, `proposed_resolution_if_any`. Unterschied zwischen real nachgewiesenem Fehler und rein hypothetischem Risiko markieren. Keine Änderung des fachlichen Plans durch den Hardener.

## Disposition durch Planner

Jede Finding-ID wird in einer eigenständigen Entscheidung einem konkreten neuen Planstand und einem Ergebnis zugeordnet: `ACCEPTED_FOR_FIX`, `ALREADY_COVERED`, `REJECTED_WITH_REASON`, `DEFERRED_BY_APPROVAL` oder `BLOCKING`. Kritische oder strittige Dispositionen unabhängig nachprüfen. Eine unbelegte Ablehnung oder ein widersprüchlicher Gesamtplan kann keine Planfreigabe begründen.

## Negativaufträge

Gezielt nach interpretierbarer Mehrdeutigkeit, ungetesteten Races, inkompatiblen Datenformaten, übersehenen Plattformen, unnötig erzwungenen Modulen, veralteten Pins und fehlenden End-to-End-Bindungen suchen. Aufgabe ist Finden und Belegen, nicht eigenständiges Planen der Korrektur.
