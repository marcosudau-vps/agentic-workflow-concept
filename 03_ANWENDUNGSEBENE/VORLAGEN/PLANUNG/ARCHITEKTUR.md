# Architektur und Systemgrenzen

## Komponenten-/Ownerkarte

| Komponente | Verantwortung | Daten/Events | Fehler-/Recoverygrenze |
| --- | --- | --- | --- |
| COMPONENT-001 | eindeutige Autorität für Ergebniszustand | K-001 | REQ-001 |

## Daten- und Kontrollflüsse

Ausführliche Übergänge, Thread/Prozess-/Netzgrenzen, Zuständigkeiten, Ursachenketten, Retry-/Timeout-/Shutdownbedingungen, Persistenz und negative Pfade beschreiben.

## Strukturkritische Invarianten

| ID | Invariante | Test | Kontrakt |
| --- | --- | --- | --- |
| INV-001 | kein doppelter Finaleffekt | TEST-001 | K-001 |

## Alternative interne Realisierungen

Nur Umsetzungsvorschläge (V3/V4) hier als solche kennzeichnen, nicht als Pflichtvertrag.
