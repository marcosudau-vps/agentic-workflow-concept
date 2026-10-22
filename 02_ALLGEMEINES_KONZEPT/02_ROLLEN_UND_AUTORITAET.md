# Rollen, Grenzen und Befugnisse

## Systemprinzip

Eine Rolle ist ein Vertrag aus Ziel, erlaubten Entscheidungen, Leseumfang, erlaubten Mutationen, Abschlusskriterien und Übergabe. Ein Modell oder ein Personenname ist keine Rolle. Eine Session kann eine Rolle erfüllen; unabhängige Prüfrollen benötigen eine von der geprüften Arbeit fachlich getrennte Session. Derselbe GitHub-Account ersetzt keine personell unabhängige formale GitHub-Approval.

## Fachliche Planung und Verfahrensautorität

Das Framework bestimmt die **Verfahrensautorität**: Wer im Entwicklungsprozess welche Entscheidung treffen, prüfen, dokumentieren und freigeben darf. Die **Projektfachautorität** liegt bei der zentralen Planung, in der Mensch und Planner-Agent als Team den Projektinhalt bestimmen. Der Planner integriert und pflegt die Ausarbeitung im autorisierten Umfang; der Auftraggeber behält übergeordnete Entscheidungen und reservierte Freigaben. Architect und Hardener unterstützen beziehungsweise prüfen, ohne selbst die fachliche Gesamtplanung zu ersetzen.

Eine Rolle erhält standardisierte Instrumente und gezielte Lesepfade. Daraus folgt keine automatische Pflicht, jedes Instrument immer zu benutzen. Die konkrete Verwendung ergibt sich aus Rollenvertrag, Auftrag und dem jeweiligen Gate.

## Rollenverträge

| Rolle | Verantwortet | Darf nicht eigenständig |
| --- | --- | --- |
| Auftraggeber | Ziele, Scope-Änderungen mit Außenwirkung, Planfreeze, kanonische Freigaben, Release-/Publishfreigaben | Technisches PASS ohne nötige Nachweise behaupten |
| Planner | Gesamtplan, Prioritäten, Requirements, Architektur-/Paket-/Nachweisintegration, Befunddisposition | Reviewer-Findings stillschweigend löschen; autoritative Freigaben erfinden |
| Architect | Architektur, Schnittstellen, Datenmodell, Datenflüsse, Kompatibilitäts- und Risikobefunde | Gesamtplan ohne Plannerentscheidung verändern |
| Hardener | Kritische Gegenbeispiele, Lücken, Widersprüche, Interpretationsrisiken und Prüfberichte | Plan oder Produktcode direkt korrigieren; Findings selbst als erledigt deklarieren |
| Planreviewer | Unabhängige abschließende Konsistenz-/Vollständigkeitsbewertung | Eigene Planrevision als unabhängigen Pass deklarieren |
| Orchestrator | Nächsten zulässigen Schritt aus aktueller Git- und Evidenzlage bestimmen | Gitrechte/Freigaben aus Statusfeldern erzeugen oder fremden Owner verdrängen |
| Implementer | Vollständige Paketumsetzung, Tests, Dokumentation, Evidenz, Abgabe | ROOT_PASS und kanonische Übernahme eigenmächtig ausstellen |
| Technical Reviewer | Unabhängige Prüfung, präzise Findings, ROOT_PASS oder BLOCKED | Produkt-/Test-/Kontraktfixes in Reviewrolle durchführen |
| Canonicalizer | Auf genau benanntem Head/Parent nach menschlichem Auftrag Aggregation und Nachweis | Anderes Paket, Release, Main, Deploy oder Cleanup automatisch mitziehen |
| Feature Qualifier | Unabhängige Gesamtprüfung der vollständigen Featureintegration, inklusive aller AP-Provenienzen und übergreifender Produkt-/Buildgates | Featureänderungen und Releaseaufnahme selbst freigeben |
| Release Qualifier | Integrierten Kandidaten, Matrix, Herkunft und Auslieferungsbereitschaft prüfen | Veröffentlichung aus `QUALIFIED` selbst auslösen |

Die Rollenbezeichnungen bezeichnen **logische Zuständigkeiten**; ein beauftragter Implementer kann später zusätzlich die kurze Canonicalizer-Rolle übernehmen, nachdem ein unabhängiger PASS und der getrennte menschliche Abschlussauftrag vorliegen. Die Rollen dürfen nicht dadurch verschmolzen werden, dass eine Session ihre eigene fachliche Arbeit reviewt.

## Autoritätsordnung

1. Tatsächlicher, im Kontext gültiger menschlicher Auftrag mit konkretem Scope und begrenzten Rechten.
2. Freigegebene Planungsbaseline sowie verbindliche Kontrakte und Projektregeln.
3. Aktuelle, belegte Git-/PR- und Runprovenienz.
4. Operative Rollen-Skills und kontextspezifische Lesepfade als Anweisungen zur Ausführung der oberen Regeln.
5. Historische Erkenntnisse/Beispiele – nur unterstützende Informationen.

Ein tatsächlicher Auftrag erteilt nur solche Rechte, die das System für diese Rolle und diesen Übergang vorsieht; eine fachliche Ausnahme benötigt die dafür vorgesehene Änderungsentscheidung. Ein unbestimmter Kurzauftrag setzt ausdrücklich reservierte Freigaben nicht außer Kraft.
