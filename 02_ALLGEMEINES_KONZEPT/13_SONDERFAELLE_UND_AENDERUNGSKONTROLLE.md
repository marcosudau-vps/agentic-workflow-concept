# Sonderfälle, Recovery und kontrollierte Planänderung

## Unterbrochene Agentenarbeit

Ein belegter Schreibowner wird durch Zeitablauf nicht abgelöst. Bei expliziter menschlicher Recoveryfreigabe sichert der neue Agent Ausgangs-PR, Gitstand, lokal erreichbare WIP, Originalübergabe, offene Findings und neuen Run. Fremde uncommittierte Daten dürfen nicht still überschrieben werden. Eine fortgesetzte fachlich identische Session kann ihren Run weiterführen; eine neue übernehmende Session erhält eine eigene Provenienz.

## Konkurrierende Paketkandidaten

Mehrere Experimente desselben AP dürfen existieren, aber nur ein Kandidat ist mit eindeutiger Belegquelle `selectedCandidate=true`. Ein neuer Versuch ersetzt den gewählten nicht automatisch. Ein ausdrücklicher menschlicher Auswahlwechsel vermerkt alten/neuen Branch, SHAs, Parent und Gründe und kennzeichnet den alten Kandidaten `SUPERSEDED`. Kein Kandidat erbt fremden PASS oder Freigaben ungeprüft.

## Crossrepo-Blocker

Wird während der Client-/Komponentenentwicklung ein Fehler einer anderen Repositorybasis reproduziert, verbleibt die aktuelle Paketlinie in einem begründet eingeschränkten Zustand. Eine gesondert beauftragte Fixinstanz im zuständigen Repository bearbeitet den Defekt mit eigener Implementierung, Evidenz, Review und Integrationsfreigabe. Die Rückkehr zum gehaltenen Ursprungspaket prüft das neue Versionspaar und wiederholt betroffene Vertragstests und Regressionen. Eine alte Paarqualifikation überträgt sich nicht durch bloßen SHA-Austausch.

## Planabweichung im laufenden Ablauf

Eine Änderung an Scope, Nutzerverhalten, Vertrag, Datenmodell, Paket-Owner, Sicherheitsgrenze oder Pflicht-DoD wird mit Folgenanalyse an den Planner zurückgegeben. Der Planner bewertet Betroffenheit, Aktualisierung von Matrix/Verträgen/Paketaufträgen und nötige Planhärtung. Bei übergreifender oder hoher Wirkung entscheidet der Auftraggeber. Nach neuer Planbaseline werden betroffene Implementierungen/Reviews requalifiziert. Lokale V3-/V4-Entscheidungen bleiben innerhalb des beauftragten Implementer-Spielraums.

## Nachträglicher Fix

Bereits angenommene Paket- und Featureaggregate bleiben unverändert. Ein erforderlicher Fix ist eine neue begrenzt beauftragte Einheit mit Verweis auf alte Requirements/Finding-/Produktidentität, erforderlichem Independent-Review und eigener Übernahme. Keine Umschreibung alter PASS-Berichte oder History.
