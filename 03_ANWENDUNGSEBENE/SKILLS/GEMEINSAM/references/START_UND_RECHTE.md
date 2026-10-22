# Verbindlicher Start und Rechteprüfung

1. Tatsächlichen Nutzer-/Systemauftrag, vorhandenes Projekt-`AGENTS.md`, Zielrepository und branch-/Dateiscope ermitteln.
2. Tatsächliche Git-Remote-Refs, lokalen HEAD/Tree/Workingtree, Commit-/PR-Lage und fremde WIP unterscheiden. Bei nicht erreichbarem Gitstand oder konkurrierender WIP keine erfolgreiche Prüfung vortäuschen.
3. Plan- und Produktbaselines sowie ihre tatsächlichen SHA/Tree/Schema-/Runtimeidentitäten aus gültiger Paket-/Planakte ermitteln.
4. Für Bearbeitung die vorhandene Arbeitsfreigabe mit **Originalquelle** prüfen. Freigabe für Kandidatencommit/normalen Push/PR kann ausdrücklich workflowweit gelten; sie gewährt keine Freigabe für `main`, Release, Tag, Deployment, Force-Push, PR-Merge oder Cleanup.
5. `writeOwner`-Status und gegebenenfalls Übergabe prüfen; fremde aktive Session und ihre uncommittierten Daten nicht verdrängen.
6. Die fachliche Aktion im Bericht samt Eingangsstand und benutzten Rechten festhalten.

Fehlt eine Voraussetzung: konkrete Lücke, zuständigen Owner und zulässigen nächsten Schritt melden. Keine Gitaktion allein weil sie technisch möglich wäre.
