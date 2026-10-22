# Test-/Artefakt-/Runtime-Nachweise

## Vor REVIEW_READY

Vollständige betroffene Regression auf vorgesehener Runtime, gezielte Fault-/Negative-/Race-Prüfungen, Build/Install/Smoke sowie Crossrepo-, Hardware- und Betriebsszenarien gemäß Plan. Tatsächliche Testmethode, Kommando, erwarteter/erzielter Wert, Exitcode, Testzahl, Runtime/Plattform, SHA/Tree, Bindungsdigest und vollständiges Log dokumentieren. Ein fehlender notwendiger Plattformzugang führt zu `NOT_RUN`, nicht zu einem angenommenen PASS.

## Reviewer

Fremde Tests unabhängig anhand Quell-/Log-/SHA- und Laufzeitbelegen prüfen; eigene zusätzliche Tests bei konkretem Verdacht. Keine pauschale erneute Windows-Vollsuite, wenn gültige Durchführung nachgewiesen ist und keine neuen Zweifel entstanden sind.

## Änderung

Code-/Test-/Kontraktänderungen nach einer Qualifikation können deren Identitätsbereich verlassen. Fachlich unveränderte administrative Nachträge sind separat anhand Diff und aktueller CI zu validieren. Crossrepo-Paare müssen ausdrücklich erneut qualifiziert werden, wenn eine beteiligte SHA/Runtime wesentlich geändert wird.

`PASS`/`FAIL`/`NOT_RUN`/`NOT_PROVEN`/`SKIPPED_EXPECTED`/`PASS_SCOPED` dürfen nicht vermischt werden. Öffentliche Nachweise niemals mit Geheimnissen oder privaten Nutzerdaten füllen.
