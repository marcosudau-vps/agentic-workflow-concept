# Menschliche Freigabe und kanonische Übernahme

## Gate

Ein Kandidat kann nur auf eine kanonische Integrationslinie übernommen werden, wenn (1) unabhängiger vollständiger `ROOT_PASS` gilt, (2) keine offenen Pflichtfindings bestehen, (3) der Auftraggeber die konkrete Übernahme ausdrücklich autorisiert hat, (4) Git-/PR-Identität, Parent, administrative Nachträge und erforderliche CI unverändert qualifiziert sind und (5) kein konkurrierender Integrationsvorgang die Zielbasis verändert hat.

## Menschliche Originalfreigabe

Der tatsächliche Originalprompt wird wortgetreu oder rechtmäßig redigiert archiviert. Er wird beim Abschluss an Paket/Feature, PR, Current-Head zum Freigabezeitpunkt, Parent und gültigen PASS-Report gebunden. Ein allgemeiner Kandidatenauftrag oder eine Promptvorlage ist keine implizite Mergefreigabe. Der ausdrücklich erlaubte administrative Commit zur Aufnahme der Freigabe wird vor dem Merge auf unfachlichen Scope geprüft.

## Durchführung

Der Abschlussagent prüft unmittelbar vor dem Eingriff aktuellen PR-Head/Base, Prüfidentität, alle Veränderungen seit `reviewed_sha`, CI, Branchschutz/Mergeability und die dokumentierte Freigabe. Er führt genau den erlaubten Squash-/Einzelaggregationsschritt aus, niemals einen zweiten Alternativweg. Für GitHub-Squash werden vorab Head- oder Testmerge-Checks ausgewertet; die resultierende Commit-SHA kann erst **danach** überprüft werden.

## Nachweis

Nach erfolgreichem Merge oder freigegebenem fast-forward: genau ein neuer Commit seit `canonicalParent`, genau ein Parent und dieser identisch zu `canonicalParent`, Aggregate-Tree identisch zum finalen autorisierten Kandidaten-Tree. GitHub-PR und Transportzustand belegen das Resultat. Erst dann `CANONICALIZED/ACCEPTED` behaupten. Ein Nachmerge-SHA kann im nächsten Paketbranch oder einem eigenständigen Abschlussnachweis dokumentiert werden, ohne einen zweiten Kanonisierungskorrekturcommit zu erzeugen.

Main, Releaseveröffentlichung, externe Deployments, Tags und Cleanup werden durch diesen Akt ausdrücklich **nicht** mitfreigegeben.
