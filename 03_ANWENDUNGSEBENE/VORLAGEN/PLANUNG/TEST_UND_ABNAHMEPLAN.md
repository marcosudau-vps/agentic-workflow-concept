# Test- und Abnahmeplan

## Teststufen

- Unit und negative Funktionsfälle, inklusive Race-/Bounds-/Recovery-/Migration.
- Integration/Prozess-/Protokollfälle gegen wirkliche oder klar begrenzte Testdoubles.
- Crossrepo-Paarcheck mit exakten SHA/Build-/Imageidentitäten.
- Build/Installer/Wheel/Container/Frozen/Hardware/Plattform, soweit dem Scope zugeordnet.
- Release RC-Matrix und mindestens ein qualifizierter Nutzer-/Betriebsfluss.

| Test-ID | Requirement | Methode | Testumgebung | erwartete Wirkung | Pflichtgate |
| --- | --- | --- | --- | --- | --- |
| TEST-001 | REQ-001 | kontrollierter Retry gegen doppelte Seiteneffekte | definierte Runtime | exakt ein Effekt | AP-001 |

Für jede Durchführung erst nachträglich tatsächliche Ergebnisse, Exitcodes, Log-/Hash-/SHA-/Runtimeidentität und eventuelle Ausschlüsse eintragen. `NOT_RUN`/`NOT_PROVEN` sind keine Freigabe.
