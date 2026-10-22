# Git-Hierarchie, Integrationslinien und Identität

## Hierarchisches Modell

```text
main:                 veröffentlichte, abgeschlossene Gesamt-Releases
└── release/<version>: kumulierte, vollständig qualifizierte Featureabschlüsse
    └── feature/<name>: eine ausgewählte aktive Featurelinie zur selben Zeit am Release-Integrationskopf
        └── work/<feature>/<AP-ID>: kumulative Agenten-/Review-/Korrekturkandidaten
            └── optionale isolierte Worktrees, Experiment- und Reviewzweige
```

`main` führt je freigegebener Releaseversion einen klaren Aggregatabschluss. Der Releasezweig enthält pro aufgenommenem Feature einen sauberen Feature-Aggregatcommit. Die konkrete Arbeitspaketorganisation *innerhalb* eines Features wird gemäß Planung gewählt; auch verschachtelte und parallele Kandidaten sind zulässig, wenn stabile Grenzen und sequenzierte Integrationsgates bestehen. Im strengen Grundmodell wird jeweils nur **eine** ausgewählte Featurelinie unmittelbar zur Aufnahme in einen Releasezweig geführt; neue Featurearbeiten können vorgeplant werden, aber nicht still konkurrierend die Releasebase verändern.

## Kandidatenlinien

Der Arbeitsbranch sammelt Implementierungs-, Reviewdokumentations- und Korrekturcommits. Reviewer darf nur im explizit berechtigten Dokumentationsscope an einen eingefrorenen Kandidaten fast-forward anschließen. Es gibt keine Pflicht, auf jedem temporären Arbeitsbranch eine bereinigte Historie zu führen. Saubere Aggregation ist eine Forderung an die **kanonische Integrationsschicht**, nicht an jeden Zwischenversuch.

## Identität

Jede Übergabe enthält Repository, Ref, vollständige Kandidaten-SHA und Tree, kanonischen Parent, prüfrelevante Baselineidentitäten, Test-/Runtime-/Buildidentitäten, PR-Link und Runbericht. Bei Crossrepo-Integrationen sind die exakten SHA-Paare und tatsächliche Runtime-Image-/Wheel-Digests relevant. Freie Textbezeichnungen wie „aktuell“ oder nur `HEAD` sind keine dauerhafte Identität.

## Sauberer kanonischer Abschluss

Eine angenommene Einheit erscheint als genau ein neuer Commit mit genau einem Parent gleich dem vorher vorgesehenen Integrations-HEAD; sein Tree entspricht dem vollständig autorisierten finalen Kandidaten-Tree. Ein GitHub-Squash erzeugt diese SHA erst beim Merge; Checks beziehen sich zuvor auf den tatsächlich geprüften Head beziehungsweise Testmerge. Die Nachmerge-SHA wird danach aus Git ermittelt und nicht fiktiv vorab in den Mergecommit eingebettet.

## Releases und Historie

`main` nimmt ausschließlich qualifizierte und ausdrücklich freigegebene Release-Gesamtstände auf. Tags, Veröffentlichungen, Deployments und öffentliche Registryuploads verlangen gesonderte Freigaben und Nachweise. Bereits angenommene Aggregate werden nicht für spätere Korrekturen per Amend/History-Rewrite verändert. Notwendige Fixes bilden neue eindeutig qualifizierte Einheiten.

Historische Arbeitsbranches können nach vollständigem Evidenz-/Provenienzerhalt entfernt werden. Branchlöschung ist keine automatische Folge eines Pass; offene PRs, einzigartige Commits und ungesicherte Runs sind vorher zu prüfen.
