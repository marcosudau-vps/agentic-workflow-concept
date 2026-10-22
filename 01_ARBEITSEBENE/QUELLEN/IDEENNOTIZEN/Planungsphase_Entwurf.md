## Planungsphase

Das System ist sehr planungsorientiert. Das heißt, es wird am Anfang eine intensive Planungsphase eingelegt,
wo quasi das ganze Projekt "am Reissbrett" entworfen und im voraus durchgeplant wird.
Die Planungsphase ist entscheidenend für das Endergebnis, deshalb sollte ihr besondere Aufmerksamkeit geschenkt werden.

- Eigenständiger Workflow, in dem gemeinsam das Projekt konkret ausgearbeitet wird.
- Rollen im Planungs-Workflow (mit eigenen Lesepfaden und Skills)
  - Planner Agent
    verantwortlich für die organisatorische und inhaltliche Planung und Strukturierung des Projekts in engem Austausch mit verantwortlichem Menschen
  - Hardening-Agent
    Je nach konkretem Auftrag verantwortlich für die Identifikation und Behebung von Schwachstellen, "Stress-Tests" der inhaltlichen und organisatorischen Planung

### Die komplette inhaltliche Planung des Projektes

Es soll möglichst präzise ein verbindliches Zielbild entwickelt werden, das alle Features, die Architektur, den Modulplan, Projekt-Struktur und alle wesentlichen Aspekte definiert.
Insbesondere sollen vorallem die exakten Spezifikationen für strukturell wichtige Teile, wie Schnittstellen, Datenmodell, Datenformate, Datenflüsse, API's, etc so genau definiert werden,
sodass den Implemenierungsagenten kein Interpretationsspielraum verbleibt und am Ende auch Codeteile von unterschiedlichen Agenten zusammen passen.

es werden auch die konkreten Arbeitspakete für die Agentenläufe zugeschnitten und die Prompts dazu vorbereitet, teilweise mit Lösungsvorschlägen für Probleme die bereits erkannt wurden.
Um sicherzustellen, dass alle Pakete auch am Ende zusammenpassen gab es konkrete Ziel-Vorgaben und eine Tracability-Matrix die alles erforderliche einbetoniert hat.
Aber es war uns auch wichtig, den Agent nicht mehr als notwendig einzuschränken und ihm überall wo es nicht so strickt sein musste Spielräume für die Entwicklung offen zu halten .

Bisherige Erfahrunge n haben gezeigt, dass es den Projekten immer sehr zugute kam, wenn die Planung zentral aus einem Guss entstanden ist, ohne dass man sich mit dem ganzen Kleinkram  während der Entwicklung befassen muss oder an Detail-Fragen hängen bleibt.
Man kann sich so aus der Makroperspektive heraus auf das Projekt als Ganzes fokussieren, wovom insbesondere die wichtigen übergreiffenden Teile wie Architektur oder Datenmodell enorm profitieren. Das ist viel besser als lokale Teil-Planung von verschiedenen Agents.

### Intensive Härtung von Beginn an

Ein sehr wichtiger Teil in der Planungsphase ist es auch, dass von Beginn an regelmäßige Härtungsläufe mitlaufen.
In denen sollen Agenten gezielt Schwachstellen suchen und aufdecken oder potentiell fehleranfällige Stellen identifizieren.
Es lohnt sich die Härtung möglichst intensiv und robust zu gestalten und ihr eine hohe Priorität einzuräumen. Jeder Fehler der hier nicht gefunden wird, wird später deutlich mehr Kosten.
Soweit möglich, die Härtungsläufe mit mehreren unterschiedlichen, aber starken KI-Modelle durchführen. (wie z.B. Opus 5.5 über GPT 6.1 Sol, o.ä.)

Wichtig dabei ist vorallem, dass die Hardening-Agenten zu ihren Findings aber immer nur Berichte erstellen, und diese nicht direkt selbst korrigieren dürfen.
Dadurch lag die letzte Entscheidung ob und wie korrigiert wird immer noch bei der Planung. Diese kann dann anschliessend abwägen was berechtigt ist, ob es einen Fix braucht und wie der am besten umgesetzt wird.
Damit soll sichergestellt werden, dass nicht das übergeordnete große Ganze bei einer Korrektur übersehen wird, und die Planung jederzeit den vollständigen Überblick behält.
Die Hardener sollen sich ausschliesslich auf ihren jeweiligen Auftrag fokussieren. Aus diesem Grund sind sie nicht für solche Änderungs-Entscheidungen qualifiziert.

- Beispiel:
  In der Vergangenheit auch Fälle, bei denen die Hardener ein Szenario gefunden haben das zwar theoretisch möglich war, praktisch jedoch annähernd ausgeschlossen.  
  Ein Fix dafür erforderte tiefgreiffende Änderungen und hätte ungefähr die hälfte der bereits robust gehärteten Architektur verworfen...

Typischerweise können sie z.B. auf Ziele angesetzt werden, wie:

- Im Code Inkonsistenzen zu finden, Widersprüche aufzudecken oder nach weiteren Fehlern, Schwachstellen oder vulnerablen Code-Teilen zu suchen.
- Strukturelle Analysen der Architektur, der Datenflüsse, Schnittstellen oder allgemeinen Kriterien wie Code-Qualität
- Absicherung der der Planungsdateien, durch Suche nach missverständlichen Formulierungen, Lücken, oder Interpretationsmöglichkeiten...

Dabei kann es in vielen Fällen hilfreich sein, die Hardening-Agenten gezielt antagonistisch zu prompten und ihnen spezifische Szenarien vorzugeben.

- Beispiel:
  Sie sollen die Prompt-Dateien für die Umsetzungen der Arbeitspakete gezielt auf zu viel Interpretations-Spielraum zu überprüfen,
  mit einem Auftrag nach dem Motto "Finde einen Weg das falsch zu machen ohne die Vorgaben zu verletzen"

### Bisheriges Fazit

Ich sehe mehrere Vorteile:

- Der aufwendigste Teil der Arbeit ist bereits erledigt, bevor überhaupt eine Zeile Code oder eine Datei im Repo geändert werden musste.
- Das Ergebnbis ist ein extrem robuster Plan.
- Die Umsetzung ist größtenteils nurnoch reine Form Sache die einfach abgearbeitet wird. Kein Überlegen was man als nächstes machen muss und keine Planänderungen während der umsetzung (folglich auch nicht die mindestens 10 Stellen, die nach spontanen Planänderungen erstmal mitgefixt werden müssten  :P)
- Alles ist nachvollziehbar und sauber Dokumentiert, und auch die Git-Historie bleibt clean und übersichtlich.

Bei dem  voice-stt-Projekten wurde ein größerer Umbau über roundabout 15 Arbeitspaketen nach diesem System umgesetzt, bei dem es einige Verschräkungen, Schnittstellen, übergebene Werte und in einander greiffende Logik gab die erst zum Schluss miteinander verdrahtet wurde. Ausserdem erstreckt sich das insgesamt über 2 unabhängige Projekte hinweg (client und server) zwischen denen die Kompatibilität beachtet werden muss.
Ich hätte es mir anfangs nicht vorstellen können, aber es hat tatsächlich alles zum größten Teil glatt zusammengepasst einfach problemlos funktioniert bisher.
Das hat für mich einfach die Zuverlässigkeit belegt. Deshalb bin ich da jetzt so überzeugt von.
