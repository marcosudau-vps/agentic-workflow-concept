# Featurequalifikation und Releaseaufnahme

**Eingang:** `FEATURE_REVIEW_READY`, vollständige AP-Integration in einem eingefrorenen Feature-HEAD/Tree, gültiger Planfreeze und konkreter Feature-DoD.

**Voraussetzungen:** jedes AP ist wirklich `CANONICALIZED` mit nachgewiesenem Root-PASS/Originalfreigabe/Squash-Tree; keine offenen Paketfixes; alle verbindlichen Verträge/Requirements und die Anwender-/Betriebsdokumentation sind vollständig. Releasefähig bedeutet nicht schon veröffentlicht.

**Unabhängige Prüfung:** gesamter kumulativer Feature-Parentdiff, echte Komponenteninteraktion/End-to-End-Fälle, Kompatibilitäts-/Migrations-/Betriebsgrenzen und gültige Build-/Runtimebelege; keine erfundenen Plattform-/Hardware-Erfolge. Nur vollständiges Pflichtgate erlaubt `FEATURE_ROOT_PASS`; ein Verweis auf vorangegangene AP-Reviews ist notwendige, aber nicht hinreichende Evidenz.

**Übernahme:** nach menschlicher, auf exakten Feature-Head/Release-Parent/Reviewbericht bezogener Freigabe genau eine Single-Parent-Aggregation in den Releasezweig. Postflight prüft realen Release-Parent, Aggregat-Tree und einen neuen Commit. Frühere Arbeitspaketcommits müssen auf Featurezweig nachvollziehbar bleiben; der Releasezweig führt das Feature als Gesamtcommit.

**Konflikte:** veränderter Releaseparent, neue fachliche Featureänderungen oder unbewiesene Requalifikation blockieren die Übernahme bis zur erneuten passenden Entscheidung.
