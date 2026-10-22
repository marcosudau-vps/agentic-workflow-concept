# System, Workflows, Branches - Entwurf

Hinweis: Hier handelt es sich erstmal um einen freien Entwurf beziehungsweise eine Ideensammlung zur Vorbereitung eines Gesamtkonzeptes. Widersprüchlichkeit ist hier aus diesem Grund möglich.

## Einleitung + Umsetzungsphase

An erster Stelle glaube Ich zunächst die Ausarbeitung des Gesamtkonzepts das Wichtigste.

Um das Ganze zu fixieren und in eine Art Standard zu gießen, durch eine klare Struktur und Definition von festenRegeln:

- feste Begriffe
- feste Strukturen
- feste Begriffe
- Verzeichnisse
- Formate (z.B. für Arbeitspakete )
- feste Rollen, mit Skills/ Lesepfaden die den jeweiligen Agent genau das wissen lassen was er für seine Rolle/Aufgabe braucht.
- vordefinierte Prompts zur Steuerung (Mit Variablen um Commits, PR, ARBEITSPAKETE, etc dynamisch einzufügen.)
- Es muss klar sein wo werden welche Metadaten von wem gespeichert und von wem gelesen...
- Welche Voraussetzungen gelten wofür..
- Wie prüft jeder Agent/Rolle prüft Voraussetzungen des eigenen Jobs.
- Wie organisiert man Verzeichnisse die dabei entstehen mit Arbeits- und Evidenz- Dokumenten, Belegen, Tests, Reviews, etc.
- Welche Metadaten

So und jetzt, nachdem ich dir erzählt habe, wie fest ich das alles zoomen möchte, fällt es mir relativ schwer auszuformulieren, was ich gerne ein bisschen lockerer halten möchte.
Obwohl nein, nicht lockerer trifft es nicht, nennen wir es lieber variabler oder flexibler...

Dabei ist es jetzt wichtig zu unterscheiden. Es geht nicht darum, irgendwelche formalen Anforderungen oder das System an sich abzuschwächen, sondern es geht darum, an bestimmten Stellen unterschiedliche Optionen/Variationsmöglichkeiten für den Planungsagenten zu ermöglichen.
Die Planungsphase hat bisher nch keine große Rolle gespielt, ist aber für das System wie ich es mir vorstelle ein fundamental wichtiger Teil.
Die Planungsphase soll ein vorgelagerter eigener Arbeitsablauf werden, in dem das Vorhaben insgesamt geplant wird, die spätere Arbeitsphase komplett vorbereitet wird, die Arbeitspakete eingeteilt werden, Tracabilities herausgearbeitet werden, ggfs weitere Anforderungen, testfälle etc...

Dafür solll der Planungsagent als eigene Rolle mit eigenem Skill, Wissen, etc. besonders qualifiziert werden.
Wegen der enormen relevanz der Planungsphase möchte Ich einige Stellschrauben schaffen, um die Situation an die Erfordernisse anpassen zu können.
Dazu wären aktuell meine Ideen:

- Nach dem Review einen austauschbaren Block der Elemente für verschiedene Absicherungs-Intensitäten enthalten kann... z.B:
  - Garnichts (entfällt)
  - Critical Review (Damit meine ich ein erneutes review, jedoch nicht so neutral wie das Normale, sondern durch einen Agenten der per Prompt nochmal stärker darauf angespitzt wird Schwachstellen zu suchen)
  - Human Approval (Menschliche Freigabe)
- Ich habe vor Beginn der U msätzung bei der Planung der Voice-STT Pakete verschiedene KI-Modelle mehrere Prüfläufe machen lassen um Inkonsistenzen zu beseitigen und die Planung zu härten. In Orientierung daran wäre eine eigene hardener-Rolle interessant, die die Planung am Ende insgesamt kritisch Prüft, quasi so Stress-Test mäßig durchgeführt.

Auch für die Planung müssen wir uns ein geeigneten Format überlegen,was wo und wie festgelgt werden soll...
Es sollte bedacht werden, dass die Projekte sich in ihrer Art enorm unterscheiden können... und man  sollte darauf eingehen können bzw. die Planung sollte das abbilden können.
Es sollte im Ermessen des Planungsagenten liegen und Teil der aktiven Planung sein, wie viel Spielraum an welchen Stellen den Agenten gelassen wird.
Es lässt sich nicht vorher oder allgemeingültig festlegen, da auch weitere Faktoren berücksichtigt werden müssen... z.B. das voraussichtlich für die Implementierung verwendete KI-Modell oder
ob es ein Projekt ist, das nach 50 Agenten-Runs immer noch exakt wie ein Mosaik an 3500 Stellen milimentergenau zusammenpassen muss, oder ob es drei kleine Module sind,
die auf drei Pakete verteilt wurden, wo grob einige wenige Schnittstellen zusammenpassen müssen, dass garkeine mega Absicherung oder menschliche Freigabe braucht....

Dass was ich hier bis jetzt alles beschrieben habe, ist erst mal nur das nackte Prinzip/Konzept, also erstmal nur der theoretische Unterbau....

Da ist noch nicht über ein tatsächliches Script oder geschweige denn eine App gesprochen...
Ich hatte ja bereits gesagt, dass es ein Steuerungsskript geben soll, das erst mal noch größtenteils manuell unterstützend durch den Ablauf führt,
sodass man jederzeit die richtigen Prompts mit den richtigen Angaben zur Hand hat, mal einen Status angezeigt bekommt oder solche Kleinigkeiten, die einen in dem ganzen Ablauf unterstützen.
Wie du aber jetzt vielleicht erkennen kannst, ist das nur noch eine Kleinigkeit am Ende und nicht der Rede wert..

Das Ganze soll dann hinterher
Später kann man das dann irgendwann schrittweise in Teilen automatisieren, aber das spielt aktuell noch keine Rolle.

## Beispiel-Workflow-Ideen

- Workflow-Beispiele

```workflow
┌---------------------------------------------------┐
|                            NEXT_AP                ▲
└─► Arbeitspaket                                    |
    │                                               |
  ┌►└── implementer                                 |
  |     │                                           |
  |     │REVIEW_READY                               |
  |     │                                           |
  |     │                                           |
  |     └── reviewer                                |
  |         │                                       |
  |         │                                       |
  |         │                                    Merge PR
  |         │                                       ▲
  |         │                                       |
  |         │   REVIEW_PASS                         |
  |         ├─────────┐                             |
  |         |         │                             |
  |         |         ├─────────────────────────►ROOT_PASS
  |         |         │                             ▲
  |         |         │                             │
  └---------┘         ├───────────────┤├────────────┘
  CHANGES_REQUIRED    │         HUMAN_APPROVAL      ▲
                      │                             │
                      │                             │
                      │                             │
                      └───────────────┤├────────────┘
                                CRITICAL_REVIEW
```

```workflow

AP-XXX-XXX
└── Am Anfang vor RUN_01
    │    - Die Dokumente (...) lesen und verstehen, norfalls Rückfragen stellen
    │    - Workspace einrichten, Ausgangsstand klonen
    │    - Arbeitsakte vorbereiten (Ordner mit INDEX.md und AP-XXX-XXX.md anlegen) 
    │
    │
    ├── Implementierung (Per Run)
    │   │    PROMPT.md
    │   │    Abschlussbericht.md
    │   │    ...
    │   │
    │   └── EVIDENCE
    │       │    - RUN-Ordner erstellen
    │       ...
    │
    ├── Implementierung
    │   │    - Arbeitsfortschritt dokumentieren
    │   │
    │   └── EVIDENCE
    │       │    ...
    │       ...
    │
    ├── Implementierung
    │
    └── nach ROOT-PASS
        │    PROMPT.md
        │    Abschlussbericht.md
        │
        └── EVIDENCE
            │    ...
            ...
```

## Prompt-Beispiele

Das sind in etwa die Prompts, die ich bei den ca. 12 Pakete die jetzt abgearbeitet wurden immer wieder verwendet habe...
Soll nur ein Beispiel sein, weil ich dir ein fach nur schnell gemacht habe... Aber so nach der Art kann man ja auch bessere vorformulieren bei denen man sich mehr Mühe gibt...
 Wichtig ist das Prinzip, vorformulierte Vorlagen und später ein Scriüpt, dass immer die richtigen Prompts automatisch zur richtigen Phase bereitstellt.

### Implementierung

Bitte setze {ARBEITSPAKET_ID} im Repository `https://github.com/marcosudau-vps/voice-stt-client` ausgehend vom aktuellen Stand von feat/client-v2 um.
Lies zuerst "ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/PLANUNG/SKILLS/voice-stt-client-v2-naechster-schritt/SKILL.md" und folge den dort verlinkten Vorgaben für Umsetzung, Tests, Dokumentation und PR-Abgabe.

### Review

Bitte prüfe den eingereichten {PULLREQUEST_ID} zum umgesetzten {ARBEITSPAKET_ID} im Repository `https://github.com/marcosudau-vps/voice-stt-client` (Branch feat/client-v2).
Lies zuerst ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/PLANUNG/SKILLS/voice-stt-client-v2-naechster-schritt/SKILL.md und folge den dort verlinkten Vorgaben für Abnahme/ Review.

### Korrektur

Die unabhängige Prüfung des Pull-Requests hat leider noch keinen Pass erteilt, sondern einen erneuten Korrekturlauf gefordert.
Die konkreten Findings Anweisungen zu den erforderlichen Korrekturen wurden hinterlegt.
Bitte lies alle Anmerkungen aufmerksam.
Aufwendigere Korrekturen sollten vor der Implementierung geplant und ggfs. auftretende Side-Effects berücksichtigt werden.
Alle vom Reviewer aufgeführten Findings müssen vollständig behoben werden.

Ausnahmen:
In folgenden Fällen soll eine Korrektur zunächst nicht durchgeführt werden:

- Findings unberechtigt zurück in die Korrektur gegeben worden
- Die Korrektur nur unter unverhältnismäßig hohem Aufwand möglich ist
- Die Korrektur tief in die Architektur eingreifft
- Die Korrektur nur entgegen der aktuellen Entwicklungs-und Architekturlinie oder Entscheidungen  möglich ist. (in relevantem Ausmaß)
Alle genannten Rechtfertigungen für das aussetzen einer Korrektur müssen ausführlich begründet werden und führen zu einer weiteren unabhängigen Prüfung die dann erneut darüber entscheidet.

Bitte führe den Korrekturlauf für {ARBEITSPAKET_ID} durch und korrigiere alle Findings.

### Review nach Korrektur

Die angeforderten Korrekturen wurden umgesetzt
Bitte prüfe den aktualisieren Stand des eingereichten {PULLREQUEST_ID} zum {ARBEITSPAKET_ID} im Repository `https://github.com/marcosudau-vps/voice-stt-client` (Branch feat/client-v2) erneut.
Sollte dies dein erstes Review in dieser Session sein und die vorgeschriebene Arbeitsweise noch nicht in deinem Kontext befinden, lies zuerst die nachfolgend genannte Skill-Datei und folge den dort verlinkten Vorgaben für Abnahme/ Review:
"ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/PLANUNG/SKILLS/voice-stt-client-v2-naechster-schritt/SKILL.md"

### Merge

- KURZ:

Hiermit wird die Freigabe zun Merge von {PULLREQUEST_ID}, Arbeitspaket {ARBEITSPAKET_ID} erteilt.
Bitte führe den Merge durch.

- LANG:

ROOT_PASS für {PULLREQUEST_ID}, Arbeitspaket {ARBEITSPAKET_ID} erteilt.

- Bitte prüfe  ob die Status- und Fortschritts- Tracking Dateien usw. korrekt aktualisiert wurden. Wenn Einträge fehlen ergänze sie selbst.  
- Prüfe zudem nochmal oberflächlich ob Umfang, Bewertungsmaßstäbe, Tracabilities, etc. insgesamt einen schlüssigen und passenden Eindruck machen oder ob es irgendwelche offensichtlichen Auffälligkeiten gibt.
- Keine fachliche Detail-Prüfung mehr, nur ein kurzer Overall-Check!
  Der Stand hat an dieserstelle schon mehrere Testphasen und ein ausführliches Review erfolgreich bestanden.

Sollte es keine weiteren Einwände geben,ist die Freigabe des abgenommenen Standes von {PULLREQUEST_ID} hiermit ausdrücklich erteilt und ich bitte dich den Merge durchzuführen.

############################

Ich kann mir das vom Konzept her aber auch sehr gut vorstellen, dass man da vielleicht, also dass man das Ganze reletiv flexibel an die Situation und die Gegebenheiten anpassen anpassen kann.

Vielleicht wird irgendwann eine Automatisierungsmöglichkeit ausgebaut die über ein Adaptermodul für Opencode-, Codex-, Copilot- und Claude-Code- CLI statt mir dann den Agent beauftragen kann...

## Branch-Strategie

### Bisherige Branch-Strategie

Die bisherige Branch-Strategie/ Arbeitsweise:

```branches
main
└── feat/[feature-name]
    │    genau ein Commit pro freigegenbenem/ abgeschlossenem Arbeitspaket
    │    Erst nach ROOT-PASS -Freigabe erlaubt
    │
    └── [feature-name]-review-candidates
        │    genau ein Commit pro abgeschlossener Agentenaufgabe / Root-Review-Kandidat
        │    Agent reicht hier einen Stand zum ROOT-REVIEW ein, nachdem er die dafür nötigen Voraussetzungen erfolgreich geprüft hat
        │    (RUN_01 -> RUN_02 -> RUN_03 -> weitere Korrekturruns kumulativ)
        │
        └── temporäre work/review/ci Branches + Worktrees
            # nur Isolation / Zwischenarbeit
            #  dürfen bei Bedarf erstellt werden
            # müssen nach ROOT PASS-Freigabe wieder entfernt werden
```

## Arbeitsakten

- Die Arbeitsakten sollen immer eine enthalten, die eine Übersicht  gibt über den Status, Statusänderungen mit datum, einen Tree mit allen enthaltenen Dokumenten, weitere/besondere Hinweise etc.
- Die Arbeitsakten sollen auch die Arbeitspaket-Beschreibung enthalten
- Run-Ordner
  Es soll für jeden Agenten-Run ein Run-Ordner mit fortlaufender Nummerierung angelegt werden mit allen Dokumenten zu diesem Run.
  - Original-Prompt
  - Evidenz-Dateien
  - Abschlussbericht
    - SHA von Ausgangsstand und Endstand
    - SHA von Ausgangsstand und Endstand
    - Kurzbeschreibung
    - Abgeschlossene Tracability-ID's
    - Besondere Hinweise (falls etwas offen ist, Ziele/ Entscheidungen geändert wurden, etc...)
- Frontmatter - Alle Dateien in der Arbeitsakte sollen einen Frontmatter mit allen wichtigen Metadaten erhalten.
  - Arbeitspaket
  - RunID
  - Datum
  - Weitere Fellder nach Bedarf.

### Struktur-Beispiel

```tree
└── AP-XXX-XXX
    │    INDEX.md
    │    AP-XXX-XXX.md
    │
    ├── RUN_01
    │   │    PROMPT.md
    │   │    Abschlussbericht.md
    │   │    ...
    │   │
    │   └── EVIDENCE
    │       │    ...
    │       ...
    │
    └── RUN_02
        │    PROMPT.md
        │    Abschlussbericht.md
        │
        └── EVIDENCE
            │    ...
            ...
```

### Idee neue Branch-Strategie: Organisatorischer Überbau mit 3 Ebenen

- Feature-Branch
  Jeder Feature-Branch soll  eine in sich schon  sein.
  - Es darf immer nur einen offenen Feature-Branch auf dem  Release-Branch geben. Dieser stellt die Spitze der Entwicklung dar und ist für laufende Entwicklung der einzige relevante Bereich.
  - Der Umfang eines Feature-Branches ist prinzipiell unbegrenzt. Es kann theoretisch ein kleines Mini-Feature mit 50 Code-Zeilen sein, oder 20 große Arbeitspakete die jeweils nochmal 20 Unterpakete haben.
  
  - Die Organisation innerhalb des Branches ist frei/ nicht vorgeschrieben... Dort können je nach Umfang des Vorhabens auch über mehrere Ebenen tief,  weitere Branches organisiert werden. (Bei mehreren Ebenen Tiefe sollte das Ein-Cleaner-Commit-Prinzip beibehalten werden bis in die tatsähliche Arbeitsebene.)     können z.B. auch mehrere Br. für Paralell-Entwicklung angelegt werden.
  - Bei Abschluss ist ein Feature-Branch eine völlig unabhängige, abgeschlossene Einheit in release-fähigem Zustand, bestmöglich getestet und validiert, enthält vollständioge Arbeits-/Evidenz-Unterlagen und eine Anwender-orientierte Dokumentation des Inhalts/Features
  - mit einem einzelnen sauberen Commit auf den Release-Branch gemerged.
    Dieser Commit sollte als Abschluss/ Endabgabe betrachtet werdenund den selben Ansprüchen genügen wie ein Release.Danach sind Korrekturen nichtmehr möglich. Er sollte nicht leichtfertig und nur nach prüfen einer Ceckliste durchgeführt werden. (Von  Agents am besten nur nach unabh. Validierung)
    Deshalb wird er bestmöglich vorbereitet, Risiken vorher ausgeschlossen, Tests, CI, etc...

- Release-Branch
  Der Release-Branch liegt zwischen den Releases und umfasst alles zwischen zwei Release-Versionen. Er beginnt mit der ersten Änderung nach einem Release und endet mit dem Merge-Commit auf Main des nächsten Releases.
  Was in eine Release-Version kommt oder wann eine neue Version released wird (=Release-Umfang) ist immer eine Einzelfall-Entscheidung.  
  Man kann auf dem Release-Branch theoretisch erstmal so viele Features ansammeln wie man möchte

- Main-Branch
  Für Releases
  Ein Commit pro Release-Version
  Clean, und vollständig validiert.

- Ich habe hier mal versucht e s ungefähr darzustellen:

```branches

                                                   dirty_br     temp_br          any_br
                                                   │            │                │
                                                   │            │                │
                                                 AP1_br        AP2_br          AP3_br                             dev_br
                                                   │            │                │                                │
                                                   │            │                │                                │
                                      ┌──feat_br1──┴────────────┴────────────────┴─────────────┐    ┌──feat_br2───┴────┐   ┌──feat_br3────────┤...├───────┐
                       ┌──release_br──┴────────────────────────────────────────────────────────┴────┴──────────────────┴───┴──────────────────────────────┴─────────────┐
──main_br────────|──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────|────────►
                 ▲                                                                                                                                                      ▲
                 │                                                                                                                                                      │
              Release V2.0.0                                                                                                                                          Release V2.0.1
```

## Beschreibung eines Agents zum Client-V2-Workflow

```markdown

### Was ich aus deinem Voice-STT-Workflow bereits nachvollziehen konnte

Ich habe das Repository [marcosudau-vps/voice-stt-client](https://github.com/marcosudau-vps/voice-stt-client?utm_source=chatgpt.com) auf dem Branch `feat/client-v2` geöffnet und die zentralen Governance-Dokumente sowie die drei Agenten-Skills gelesen.

Das Entscheidende an deinem System ist nicht die umfangreiche Dokumentation an sich, sondern die Trennung zwischen zentraler Planung, verbindlichen Verträgen, delegierter Umsetzung und unabhängiger Abnahme.

Damit korrigiere ich auch meine bisherige Vorstellung vom LEFX-Studio-Projekt: Wir sollten nicht lediglich einige Planungsdateien anlegen und anschließend schrittweise Architekturentscheidungen bei der Implementierung treffen. Stattdessen erarbeiten wir zunächst ein zusammenhängendes, belastbares Gesamtkonzept und schneiden danach die Agentenaufträge daraus zu.

Besonders wichtig finde ich, dass euer Regelwerk vier Arten von Vorgaben unterscheidet:

| Art                                      | Verbindlichkeit                          |
| ---------------------------------------- | ---------------------------------------- |
| Schnittstellen und Verträge              | Exakt einzuhalten                        |
| Produktanforderungen und Schutzwirkungen | Ergebnis verbindlich, Umsetzung flexibel |
| Technische Lösungsvorschläge             | Begründete Alternativen zulässig         |
| Technische Startwerte                    | Anhand von Tests und Messungen anpassbar |

Genau damit löst ihr das Spannungsverhältnis zwischen einem gründlich durchgeplanten Projekt und einem Agenten, der beim Umsetzen eigenständig vernünftige technische Entscheidungen treffen können soll.

Auch eure Trennung von `REVIEW_READY`, `ROOT_PASS` und `ACCEPTED` ist wesentlich: Selbstprüfung, unabhängige technische Abnahme und menschlich freigegebene Übernahme sind ausdrücklich unterschiedliche Schritte.

Die Arbeitsakten sind dabei keine lose Sammlung von Logs. Jeder tatsächliche Agentenlauf erhält seinen Originalauftrag, einen Abschlussbericht und einen zugehörigen Evidenzindex. Korrekturen und weitere Reviews erzeugen neue Akten, ohne die historischen Ergebnisse umzuschreiben.

### 2. Die konkreten Unterlagen bestätigen die Arbeitsweise

Ich habe zusätzlich den Gesamtimplementierungsplan, zwei Arbeitspakete, die Traceability-Matrix, die maschinenlesbaren Requirements, historische Planungsprüfungen und einen vollständigen Ablauf von Umsetzung bis unabhängiger Abnahme untersucht.

Drei Dinge stechen dabei besonders hervor.

#### Die Planung ist tatsächlich paketübergreifend geschlossen

Der Client-V2-Plan umfasst 12 Entwicklungs- und zwei Integrationspakete. Er definiert bereits vor der Implementierung die fachlichen Übergaben zwischen Transport, Mirror, Audio, Settings, Feedback und UI.

Die 216 einzeln identifizierten Requirements besitzen jeweils eine Zuordnung zu Vertrag, Arbeitspaket und vorgesehenem Nachweis. Die Matrix existiert sowohl menschenlesbar als Markdown als auch strukturiert in `requirements.json`.

Das ist mehr als eine Aufgabenliste. Es entsteht eine überprüfbare Kette:

Produktziel und Anforderung

Verbindlicher Kontrakt und Datenmodell

Zuständiges Arbeitspaket

Tatsächliche Implementierung und Testmethode

Evidenz und unabhängige Abnahme

#### Die Agenten erhalten nur das Wissen, das sie benötigen

Die drei Skills bilden einen klaren Einstieg: nächster Schritt, Umsetzung und Abnahme. Dahinter liegen gemeinsame Referenzen und rollenspezifische Checklisten.

Der Umsetzer muss nicht jedes Mal den gesamten Gesamtplan lesen. Er bekommt sein konkretes Paket mit den notwendigen Verträgen, Abhängigkeiten und Abnahmekriterien. Der Reviewer erhält einen anderen Lesepfad.

Das ist auch eine gute Antwort auf die sonst schnell entstehenden riesigen Agenten-Prompts.

#### Git-Historie und Arbeitsakten ergänzen sich

Die Entwicklungsbranch enthält die angenommene, kumulative Projektentwicklung. Jedes Arbeitspaket wird dagegen auf einem eigenen Arbeitsbranch entwickelt und geprüft.

Erst nach unabhängiger Abnahme und deiner Freigabe wird ein sauberer Paketcommit übernommen.

Die Runakten erhalten die detaillierte Historie einschließlich Zwischenkorrekturen, Belegen und Reviewentscheidungen. Das eigentliche Git-Protokoll bleibt übersichtlich.

Gerade an [`AP-CV2-030`](https://github.com/marcosudau-vps/voice-stt-client/tree/feat/client-v2/ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/30_AUSFUEHRUNG/AP-CV2-030?utm_source=chatgpt.com) lässt sich dieser Ablauf gut nachvollziehen.

### 3. Die Planungs-Härtung ist ein eigenständiger Prozess

Hier ist deine zusätzliche Erklärung besonders wertvoll. Die fertigen Planungsdokumente beschreiben das Ergebnis der Härtung deutlich besser als die Vorgehensweise, die dazu geführt hat.

In den historischen Prüfungen habe ich beispielsweise einen externen Prüfbericht gefunden, der unter anderem unklare Regeln für unterbrochene Agentensessions, Kandidatenwechsel und Serverkorrekturen aufdeckte.

Daneben liegt eine gesonderte Bewertung, in der diese Findings einzeln eingeordnet und die erforderlichen Korrekturen festgelegt wurden.

Das bestätigt dein beschriebenes Prinzip: Der prüfende Agent entscheidet nicht darüber, welche Architekturänderung vorgenommen wird.

Für das LEFX-Studio würde ich deshalb schon während der Planung einen geregelten Härtungszyklus vorsehen:

Zentrale Planung erstellt oder überarbeitet den Gesamtentwurf

Unabhängige Agenten prüfen gezielt unterschiedliche Schwachstellen

Findings werden unverändert und nachvollziehbar dokumentiert

Zentrale Planung bewertet Risiko, praktische Relevanz und Korrekturkosten

Nur angenommene Korrekturen fließen kontrolliert in den Plan zurück

Dabei würde ich deine unterschiedlichen Prüfschwerpunkte übernehmen: fachliche Inkonsistenzen, fehlende Randfälle, Schnittstellenprobleme, Traceability-Lücken, methodische Schwächen und adversariale Prompt-Prüfungen.

Gerade der Ansatz „Finde eine falsche Implementierung, die formal trotzdem alle Vorgaben erfüllt“ ist für unsere späteren Agentenaufträge sehr interessant.

Es muss aber auch den gegenteiligen Prüfauftrag geben: Wo haben wir einen Agenten ohne fachlichen Grund unnötig eingeschränkt?

Und deine Erfahrung mit übertriebenen theoretischen Korrekturen gehört ausdrücklich in die Bewertungsregeln. Nicht jeder technisch denkbare Sonderfall rechtfertigt einen aufwendigen Umbau.

### 4. Was ich für das LEFX-Studio übernehmen würde

Die grundsätzliche Methode würde ich beibehalten, ihren Umfang allerdings an unser Projekt anpassen.

| Bestandteil                                     | Für unser Studio                         |
| ----------------------------------------------- | ---------------------------------------- |
| Zentrale, vollständige Planungsphase            | Übernehmen                               |
| Bestandsaufnahme mit fixiertem Ausgangscommit   | Übernehmen                               |
| Zielbild, Architektur und Datenmodelle          | Vor Implementierung ausarbeiten          |
| Schnittstellen- und Verantwortungsverträge      | Verbindlich definieren                   |
| Traceability mit stabilen Requirement-IDs       | Übernehmen                               |
| Geplante Agentenpakete mit DoD                  | Übernehmen                               |
| Rollenspezifische Skills und Prompts            | Übernehmen                               |
| Unabhängige Planungs-Härtung                    | Bereits während der Planung              |
| Härtungsagenten ohne Änderungsrecht             | Verbindlich                              |
| Review, Nachweise und menschliche Mergefreigabe | Übernehmen                               |
| Umfang der Dokumentation und Paketanzahl        | An die tatsächliche Komplexität anpassen |

Ein Punkt ist mir dabei besonders wichtig: Wir sollten erst die fachlichen Gestaltungsmöglichkeiten des visuellen Effekteditors vollständig erfassen, bevor wir sein internes Datenmodell und seine Komponentenverteilung verbindlich entwerfen.

Ansonsten würden wir zwar zentral und gründlich planen, aber möglicherweise auf einer zu früh getroffenen Annahme aufbauen.

Für den späteren Agenten-Kollaborationsmodus würde ich zunächst nur die Projektgrenze und seine Anforderungen festhalten. Seine detaillierte Architektur kann eine eigene Planungsphase bekommen. Gleichzeitig sollten wir im visuellen Editor keine unnötigen Abhängigkeiten schaffen, die eine spätere externe Steuerung verhindern.

### 5. Konkrete Konsequenz für unser weiteres Vorgehen

Ich würde unsere Arbeit in vier aufeinanderfolgende Planungsabschnitte gliedern:

1. Projektfundament: Bestandsaufnahme, unveränderliche LEFX-Verträge, Entwicklungsbranch, Arbeitsstruktur und Ziele beider Vorhaben.
2. Fachliches Gesamtkonzept: Gestaltungsmöglichkeiten, Anwendungsfälle, Bedienkonzept, Entwurfsspeicherung und Verhalten des neuen Studios.
3. Technischer Gesamtentwurf: Datenmodell, Komponenten, Schnittstellen, bestehende Wiederverwendung, Tests und Paketgrenzen.
4. Härtung und Plan-Freeze: Mehrere unabhängige Prüfungen, zentrale Findingbewertung, Korrekturen, Traceability-Abschluss und vorbereitete Agentenaufträge.

Das ist keine starre Festlegung auf vier Dokumente oder genau vier Agentenläufe, sondern die Reihenfolge, in der die Planung belastbar werden soll.

Die Unterlagen würde ich unter `ARBEITSDATEIEN` führen, mit getrennten Bereichen für Planung, Ausführung und Evidenz – angepasst an das bestehende Repository und ohne die alte Dokumentationsstruktur unnötig zu kopieren.

#### Besonders hilfreiche Referenzdateien

- [PLANUNGSSPIELRAUM.md](https://github.com/marcosudau-vps/voice-stt-client/blob/feat/client-v2/ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/PLANUNG/SKILLS/GEMEINSAM/references/PLANUNGSSPIELRAUM.md?utm_source=chatgpt.com) – Verbindlichkeit und Entwicklungsfreiheit.
- [TRACEABILITY_MATRIX.md](https://github.com/marcosudau-vps/voice-stt-client/blob/feat/client-v2/ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/PLANUNG/REFERENZ/TRACEABILITY/TRACEABILITY_MATRIX.md?utm_source=chatgpt.com) – zentrale Nachverfolgbarkeit.
- [PAKETABLAGE_UND_VORLAGEN.md](https://github.com/marcosudau-vps/voice-stt-client/blob/feat/client-v2/ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/PLANUNG/SKILLS/GEMEINSAM/references/PAKETABLAGE_UND_VORLAGEN.md?utm_source=chatgpt.com) – Arbeitsakten und Übergaben.
- [EXTERNER_PRUEFBERICHT_REV9.md](https://github.com/marcosudau-vps/voice-stt-client/blob/feat/client-v2/ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/PLANUNG/EVIDENCE/HISTORIE/EXTERNER_PRUEFBERICHT_REV9.md?utm_source=chatgpt.com) – Beispiel für unabhängige Planungsprüfung.
- [BEWERTUNG_PRUEFBEFUNDE_REV10.md](https://github.com/marcosudau-vps/voice-stt-client/blob/feat/client-v2/ARBEITSDATEIEN/10_AKTUELL/CLIENT_V2/PLANUNG/EVIDENCE/BEWERTUNG_PRUEFBEFUNDE_REV10.md?utm_source=chatgpt.com) – getrennte Bewertung und kontrollierte Übernahme von Findings.

Mein Gesamturteil: Ich verstehe jetzt nicht nur die Dokumentstruktur, sondern auch die dahinterliegende Arbeitsphilosophie deutlich besser. Vor allem die zentrale Architekturplanung, die explizite Trennung zwischen Vertrag und Umsetzungsvorschlag sowie die unabhängige, ausschließlich berichtende Planungs-Härtung sollten wir beim LEFX-Studio als Grundprinzipien fest übernehmen.
```
