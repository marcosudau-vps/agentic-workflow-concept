# Ausnahmefälle und Wiederaufnahme

## Recovery

Ein aktiver fremder Schreibowner wird nicht wegen Alter oder Abwesenheit von Commits abgelöst. Belegte Übergabe oder spezifischer menschlicher Recoveryauftrag erforderlich. Alten Parent/Head/WIP/Findings sichern, neuer Run und neuer Owner; kein Reset/Force-Push zur „Bereinigung“.

## Kandidatenwechsel

Mehrere Kandidaten desselben AP haben verschiedene Branch-/Run-IDs; genau eine ausgewählte Linie. Neues Experiment `selectedCandidate=false` bis eindeutiger menschlicher Auswahl. Altlinie als `SUPERSEDED` dokumentieren, alte Befunde und Provenienz erhalten. Kein PASS-Transfer.

## Crossrepo-Defekt

Held-Client/Paket statusblockiert; Fix im tatsächlichen Ownerrepository nur mit gesonderter Freigabe. Neue Server-/Library-/Komponentensha in Rückkehrbeleg; geänderte Verträge, Vektoren und betroffene Client-/Integrationsprüfungen erneut durchführen. Keine eigenmächtige Serverpromotion aus Clientauftrag.

## Planchange

V1/V2-Änderung zuerst als belegten Changeantrag mit Impact auf Architecture/Requirements/APs/Tests dem Planner geben. Unabhängige Härtung nach Risikowirkung und neue Baseline-/Freigabeentscheidung. Unterdessen nur ausdrücklich unabhängige, risikoarme Arbeiten ausführen.

## Nachträglicher Fix

Neues AP mit `correctsPackage`/Affected-Requirements und voller Review-/Übernahmekette; alte Aggregate und Reports bleiben unverändert.
