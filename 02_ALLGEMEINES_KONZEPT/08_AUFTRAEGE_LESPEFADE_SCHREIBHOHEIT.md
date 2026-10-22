# Aufträge, Lesepfade, Sessions und Schreibhoheit

## Auftrag und Berechtigung

Jeder tatsächliche Agentenauftrag hat eine Originalquelle mit Scope, Rolle, Ziel/Repository, erlaubten Gitaktionen, Kandidat/Planbaseline und Abgabekriterien. Eine Vorlage ist kein erteilter Auftrag. Arbeitsfreigaben für Kandidatencommits können fortgelten, wenn ihre ursprüngliche Quelle dokumentiert und der Scope unverändert ist; kanonische Übernahme, Release, Main, Tags, Deployment und Cleanup sind stets ausdrücklich gesonderte Freigaben.

## Rollenbezogene Informationsversorgung

Ein Rollen-Skill lädt zunächst nur **gemeinsame Verfahrensgrenzen**, anschließend die für diesen Auftrag benötigte Paket-/Planungsakte, konkrete Kontraktabschnitte und zuletzt nur betroffene Produkt-/Evidenzquellen. Nicht benötigte historische Analysen, Gesamtpläne und Facharchive gehören nicht zur pauschalen Pflichtlektüre. Ein Git- oder Statuswiderspruch wird vor Ausführung geklärt, nicht durch weitere ungezielte Lektüre überdeckt.

## Sitzungsmodell

Eine Session bearbeitet genau den ihr zugewiesenen fachlichen Auftrag und dokumentiert ihn als Run. Fortsetzungsnachrichten innerhalb derselben offenen Session erzeugen nicht automatisch neue Runs. Ein unabhängiger fachlicher Review erfordert eine neue, unbeteiligte Session. Ein von demselben Mensch-/GitHub-Account angestoßener Agentreview kann technisch unabhängig sein, ersetzt aber keine GitHub-seitig nötige formale Approval durch einen zweiten Account.

## Single Writer / Freeze

Je aktivem Kandidatenzweig besitzt genau ein schreibberechtigter Run die aktuelle Schreibhoheit. Bei `REVIEW_READY` beendet der Implementer Pushes auf diesen Branch. Der Reviewer liest einen exakten SHA/Tree und schreibt ausschließlich freigegebene Reviewer- und administrative Unterlagen als nachfolgenden Fast-forward-Commit. Änderungen am Produkt verlangen neuen Kandidaten und neue fachliche Prüfung. Bei unerwartetem Fremdfortschritt wird gestoppt.

## Übernahme einer Unterbrechung

Schreibownerwechsel benötigt tatsächliche Übergabe oder expliziten menschlichen Recoveryauftrag, gesicherten Remote-/WIP-Ausgangszustand und neue Runakte. Zeitablauf, eine leere Statusdatei oder fehlender Aktivitätsindikator legitimieren keine Übernahme. Nicht zugängliche fremde lokale Arbeit bleibt als Lücke ausgewiesen.
