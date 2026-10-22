# Gesamtsystem – Aufbau und Lebenszyklus

## Gegenstand

Das Verfahren organisiert komplexe Softwareentwicklung mit spezialisierten KI-Agenten als **planungsorientierten, beweisgestützten und menschlich kontrollierten Vorgang**. Es trennt kreative Gesamtplanung, unabhängige Schwachstellensuche, begrenzte Umsetzung, unabhängige Produktabnahme, autorisierte Git-Übernahme und Releasequalifikation.

Der Prozess setzt einen vollständigen, strukturell abgesicherten Plan **vor** Beginn abhängiger Produktimplementierung voraus. Änderungen während der Ausführung werden nicht verboten, sondern an eine explizite Änderungsentscheidung und Folgenanalyse gebunden.

## Verfahrensrahmen und Projektinhalt

Das System definiert, **wie** die gesamte Projektentwicklung von Zielklärung und Planung bis Umsetzung, Abnahme und Veröffentlichung organisiert und abgesichert wird. Es gibt den fachlichen Inhalt eines konkreten Projekts nicht vor. Stattdessen definiert es verbindliche Begriffe, Zuständigkeiten, Zustände, Übergänge, Nachweisregeln und standardisierte Instrumente.

Die **zentrale Planung** ist die Zusammenarbeit von menschlichem Auftraggeber und Planner-Agent. Dieses Team gestaltet das konkrete Vorhaben nach seinen Erfordernissen: Zielbild, Anforderungen, Architektur, Schnittstellenverträge, Features, Arbeitspakete und Qualifikation. Der Planner führt den konsistenten Gesamtplan im beauftragten Umfang; der Mensch verantwortet wesentliche Richtungsentscheidungen und ausdrücklich reservierte Freigaben. Weitere Rollen liefern Fachbeiträge oder unabhängige Befunde, ohne eine konkurrierende Gesamtplanautorität zu begründen.

Das Framework stellt Instrumente wie Rollen-Skills und Lesepfade, Verbindlichkeitskennzeichnungen in Aufträgen, Traceability-Formate, Vorlagen, Schemas und Prüfskripte bereit. Ihr Einsatz ist je nach Rolle und Übergang verbindlich oder bedarfsorientiert. Die freigegebene Projektplanung befüllt die vorgegebenen Formate mit **projektspezifischen** Entscheidungen; nach Planfreeze gelten dafür die geregelten Änderungsbedingungen.

## Strukturelle Einheiten

1. **Projekt:** Repository- oder Repositoryverbund mit Zielbild, Verantwortlichkeit und gemeinsamen Regeln.
2. **Entwicklungsvorhaben:** inhaltlich abgegrenzter Auftrag, aus dem der Planner Featureplanung, Verträge und Pakete formt.
3. **Planungsbaseline:** qualifizierter, eindeutig versionierter Satz von Anforderungen, Architektur-, Schnittstellen- und Testdefinitionen.
4. **Feature:** fachlich zusammenhängende, vollständig abgenommene und für die Aufnahme in eine Release-Linie geeignete Einheit.
5. **Arbeitspaket:** einem definierten Bearbeiter zugeordnete überprüfbare Ergebniseinheit mit konkreten Voraussetzungen, Outputs und Abnahmekriterien.
6. **Run:** zeitlich und sachlich definierter Agentenauftrag mit eigener unverwechselbarer Akte, Resultat und Nachweisen.
7. **Kandidat:** identifizierbarer Gitstand oder gesicherter Diff, der für eine definierte Prüfung eingereicht wird.
8. **Gate:** überprüfbarer Übergang, dessen Voraussetzungen dokumentiert und erfüllt sein müssen.
9. **Kanonische Übernahme:** Überführung eines technisch bestandenen und ausdrücklich freigegebenen Kandidaten in die festgelegte Integrationslinie.
10. **Release:** integrierte, qualifizierte Produktfassung mit versionierter Herkunft und gesonderter Veröffentlichungsentscheidung.

## Gesamtfluss

```text
Auftrag + Istaufnahme
   -> zentrale Planung / Architektur / Verträge / Traceability
   -> unabhängige Planhärtung(en) -> Befunddisposition durch Planner
   -> Planreview + ausdrückliche Planfreigabe -> Planfreeze
   -> Feature- und Arbeitspaketbearbeitung
      -> Implementierung + Selbstprüfung + qualifizierte Nachweise
      -> unabhängiger technischer Review -> Findings/Korrektur (ggf. wiederholt)
      -> ROOT_PASS -> ausdrückliche Übernahmefreigabe
      -> geprüfter Aggregatcommit im übergeordneten Zweig
   -> vollständiges Feature-Gate -> Aufnahme in Release-Linie
   -> Release-Candidate-Build, Matrixqualifikation und unabhängiges Gate
   -> ausdrückliche Releasefreigabe -> sauberer Main-Abschluss
   -> gesondert autorisierte Veröffentlichung / Nachweis / Archiv
```

## Invarianten

- Eine Rolle darf **ihre eigene fachliche Arbeit nicht unabhängig abnehmen**.
- Ein Reviewbericht ist kein Git-Merge, eine Statusbehauptung kein Reviewbericht und ein grüner CI-Lauf keine menschliche Freigabe.
- Autoritative Kontrakte und Produktanforderungen sind verbindlich; interne Umsetzungsvorschläge begründen keine ungewollte Architekturpflicht.
- Identität gilt für **konkrete SHA/Tree-/Artifact-/Runtime-Paare**. Nach fachlicher Änderung ist die alte Qualifikation nicht automatisch übertragbar.
- Historische Berichte und tatsächliche Originalprompts werden nicht überschrieben; neue Ergebnisse erhalten neue Runakten oder dokumentierte Nachträge.
- Übergänge erfolgen nur bei belegten Voraussetzungen und gültiger Zuständigkeit.
- Der endgültige Release- und Publikationsvorgang ist von der fachlichen Entwicklungsübernahme getrennt.

## Drei Systemdarstellungen

Der Regelkern liegt in der allgemeinen, sachlichen Konzeptebene. Operative Lesepfade, Skills, Vorlagen und Prüfer setzen denselben Regelkern um. Entstehungsgeschichte und Änderungsgründe verbleiben im Arbeitskontext. Die operative Anwendung darf keine eigenständige abweichende Regelautorität erzeugen.
