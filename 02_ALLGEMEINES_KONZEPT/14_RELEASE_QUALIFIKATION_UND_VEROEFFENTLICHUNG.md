# Release-Candidate, Release-Abnahme und Veröffentlichung

## Releaseintegration

Der Releasezweig sammelt ausschließlich abgeschlossene und qualifizierte Featureaggregate. Die Entscheidung über Umfang und Zeitpunkt eines Releases liegt beim Auftraggeber. Ein Feature gilt als releasefähig nur mit eigenem unabhängigen Featuregesamt-`FEATURE_ROOT_PASS` und gesonderter menschlicher Release-Aufnahmefreigabe, dokumentiertem Nutzer-/Betriebsverhalten, Test-/Integrationsnachweis und unveränderlich verknüpfter Herkunft.

## RC-Qualifikation

Für einen Release-Candidate werden auf einer fixierten Quell-/Konfigurations-/Dependencybasis die definierten Artefakte reproduzierbar oder prüfbar erzeugt und in einer Qualifikationsmatrix nach Betriebssystem, Edition, Python-/Runtime- und Packagingvariante bewertet. Die Matrix unterscheidet vorhandene, tatsächlich geprüfte, nicht ausführbare und gescheiterte Fälle. Jedes Artefakt besitzt Digest, Buildmanifest, Quell-SHA/Tree, Toolchain- und Dependencyidentitäten sowie die dazugehörigen Test-/Smoke-/Sicherheitsbelege.

Ein grüner Workflow ersetzt keinen funktionalen Release-Gate-Report. Der Release Qualifier prüft Gesamtkohärenz, Unterschiede zwischen Quell- und ausgeliefertem Artefakt, Installer-/Wheel-/Containerlaufzeiten, Migrationsszenarien, Crossrepo-Paare, Plattformlücken, bereits akzeptierte Ausnahmen und vorherige Findings. Ein alter RC auf vorherigem Commit qualifiziert den neuen Commit nicht.

## Freigabe und Main

Nach vollständiger technischer Releasequalifikation werden offene Pflichtbefunde geschlossen. Der Auftraggeber autorisiert ausdrücklich die Aufnahme genau dieses qualifizierten Releaseinhalts auf `main`. Es entsteht ein eindeutiger Release-Aggregatcommit mit nachgewiesenem Parent-/Treebezug und Versionsidentität. Git-Tags werden an die tatsächliche freigegebene Commitidentität gebunden; ihre Erzeugung ist gesondert beauftragt.

## Veröffentlichung und Rollout

Der öffentliche Upload zu PyPI, Registry/GHCR, Paketmanager oder Releaseplattform sowie Produktionseinsatz sind **separate mutative Vorgänge**. Sie erfordern eigene Freigabe, Ziel-/Account-/Artefaktprüfung, Secret-/Supply-Chainprüfung, erwartete Version, Rückrollkonzept und Transport-/Nachpublikationsbeleg. Staging-Runs dürfen keine öffentliche Veröffentlichung stillschweigend auslösen. Bereits veröffentlichte Versionen werden nicht per History-Rewrite verändert.

## Releaseabschluss

Releaseakte und finaler Versionsnachweis enthalten Quellcommit/Tag, RC-Build- und Artefakthashes, Qualifikationsmatrix, Freigabeoriginal, Main-Aggregat, tatsächliche Veröffentlichungslocations und verifizierte Benutzer-/Betriebsnachweise. Nicht erfolgte Veröffentlichung bleibt ausdrücklich `NOT_PUBLISHED`, selbst wenn `RELEASE_QUALIFIED` ist.
