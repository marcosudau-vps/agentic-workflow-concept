# Planungsphase: Intake, Gesamtsicht, Zielbild und Verträge

## Eigenständiger Planungsworkflow

Die Planung ist ein vollständiger vorgelagerter Arbeitsprozess. Sie beginnt mit dem Auftragsverständnis und endet mit einem intern kohärenten, nachweisgestützt überprüften Plan, der die Ausführung ohne fortlaufende ad-hoc-Grundsatzplanung ermöglicht. Die Gesamtplanung wird durch den **Planner** integriert; Architekturanalysen und Spezialprüfungen werden gezielt eingebunden, ohne eine zweite konkurrierende Planautorität zu schaffen.

## Inhaltliche Zuständigkeit der zentralen Planung

Menschlicher Auftraggeber und Planner-Agent arbeiten in der zentralen Planung **als Team** zusammen. Sie gestalten das Projekt aus dessen tatsächlichen Bedürfnissen heraus und legen die projektbezogenen Anforderungen, Architektur, Verträge, Feature- und Paketgrenzen sowie Qualitätsmaßstäbe fest. Der Mensch verantwortet dabei die übergeordneten Entscheidungen und reservierten Freigaben; der Planner koordiniert und integriert die detaillierte Planung im erteilten Umfang.

Das Framework liefert dafür Begriffe, Rollenverträge, strukturierte Planungs- und Auftragsformate sowie qualifizierbare Übergänge, nicht aber produktspezifische Lösungen. Beiträge weiterer Agenten werden vom Planner in Abstimmung mit dem Auftraggeber bewertet. Nach Planfreeze werden Projektverträge nicht stillschweigend geändert.

## Eingang und Istaufnahme

Vor der Lösungsfestlegung erfasst der Planner den tatsächlichen Repository-/Produkt-/Infrastrukturstand, offene Änderungen, Zielsysteme, Nutzerziele, vorhandene Verträge, Risiken, Abhängigkeiten, Versions-/Kompatibilitätsgrenzen und Auswirkungen auf andere Repositories. Quellen bekommen Herkunft, beobachteten SHA und Gültigkeitsumfang. Vermutete Tatsachen werden nicht als beobachtete Vertragsrealität dargestellt.

## Vom Ziel zu überprüfbaren Einheiten

1. **Auftrag und Zielbild:** Funktionsumfang, Nichtziele, Nutzerabläufe, fachliche Definition des fertigen Zustands, Akzeptanzmaßstab.
2. **Systemkontext und Architektur:** Komponenten, Verantwortungsgrenzen, Datenflüsse, Thread-/Prozess-/Netzgrenzen, Lifecycle, Persistenz, Fehler- und Recoverypfade.
3. **Verträge:** Wire-/API-/Event-/Schema-/Storage-/Konfigurationsverträge, Fehlercodes, Versionsregeln, Beispiele/Vektoren und Migrationsbedingungen.
4. **Sicherheit und Betrieb:** Credentialschutz, Logs/Privacy, Ressourcenlimits, Ausfallverhalten, Plattformziele, Diagnose-, Deployment- und Wartungsannahmen.
5. **Anforderungen:** eindeutige IDs, fachliche Wirkung, Priorität, Owner, Kontraktanker, Testmethode, negative Fälle und DoD.
6. **Integrations- und Teststrategie:** Unit-, Integrations-, Prozess-, Build-, Hardware-, Fault-Injection- und Crossrepo-Belege mit Laufzeit-/SHA-Bindung; frühe Checkpoints bei Risiken.
7. **Feature- und Paketstruktur:** Abhängigkeiten, umsetzbare Teilergebnisse, handhabbare Prüfgrößen, Reihenfolge bzw. ausdrückliche Parallelfreigaben.
8. **Ausführungsaufträge:** Rollen-/Lesepfadzuordnung, Voraussetzungen, Ergebnisse, erlaubte Implementierungsfreiheit, Übergabeformate und Nachweise.
9. **Planpflege und Änderungsgrenzen:** Wer während der Ausführung Änderungen vorschlagen, bewerten, genehmigen und in betroffene Stellen einarbeiten darf.

## Zentrale Konsistenz

Die Architektur wird in einer gemeinsamen Sicht geplant, damit unabhängig implementierte Module nicht widersprüchliche Besitzer, Lebenszyklen, Namen oder Wireinterpretationen erzeugen. Für strukturell kritische Teile gibt es eindeutige Verträge und grenzübergreifende Negativfälle. Fachlich einfache interne Realisierungsdetails bleiben als V3/V4 offen. Ein geplanter Klassenname erzeugt keine künstliche Pflicht zum Re-Design vorhandener Komponenten.

## Planartefakte

Eine vollständige Planung besitzt mindestens: Planindex, Zielbild, Ist-/Baselineinventar, Architektur-/Datenflussbeschreibung, Kontrakte, Risiko- und Entscheidungsregister, Requirements-JSON, Traceability-Tabelle, Test-/Abnahmeplan, Feature-/Paketmanifest, ausführbare Paketdefinitionen und einen Planqualifikationsbericht. Dokumente verweisen aufeinander über stabile IDs; eine einzige Aussage erhält keine konkurrierenden Wahrheiten in mehreren Registern.

## Durchdringung der Risiken

Die Planung befasst sich frühzeitig mit gegenläufigen Anforderungen, Race-Conditions, ausgefallenen Komponenten, begrenzter Ressourcenverfügbarkeit, Crossrepo-Mismatches und realer Laufzeit. Für jedes priorisierte Risiko wird die präventive Vertragsregel, die mögliche Wirkung und die konkrete Validierung benannt. Erst durch diese Verbindung kann die spätere Implementierung überwiegend eine überprüfbare Ausführung des festgelegten Plans sein.
