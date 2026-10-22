# Unabhängige Planhärtung, Befunddisposition und Planfreigabe

## Zweck

Unabhängige Hardening-Läufe suchen gezielt nach Fällen, in denen das geplante Gesamtsystem fehlerhaft, unvollständig, missverständlich, inkonsistent, unsicher oder mit vorhandenen Mitteln nicht belegbar wäre. Die Prüfung ist ausdrücklich nicht auf Stil oder neutrale Plausibilität beschränkt: Sie sucht Gegenbeispiele, kritische Sequenzen, ungeregelte Eigentümerschaft und Wege, den Auftrag formal korrekt und funktional falsch umzusetzen.

## Prüfformate

- Vertrags-/Schema-/Datenflusskritik einschließlich Negativvektoren, Versionierung, Grenzen und Recovery.
- Architektur-Stresstest (Races, Ausfälle, Ressourcen, Berechtigungen, Datenschutz, Migration, Plattformen, Integrationsfolge).
- Spezifikations- und Prompt-Adversarialität („Wie kann diese Formulierung regelkonform missverstanden werden?“).
- Requirement-/Traceability-Audit einschließlich fehlender Eigentümer und nicht ausführbarer Tests.
- Paket-/Integrationsaudit: verspätet entdeckte Abhängigkeiten, unqualifizierbare Zwischenstände, widersprüchliche Parallelitätsannahmen.
- Unabhängige Gesamtprüfung des konsolidierten Plans nach Korrekturen.

Mehrere voneinander unabhängige Perspektiven und, soweit verfügbar, unterschiedliche leistungsfähige Modelle können denselben Plan mit eigenen Aufträgen prüfen. Eine mehrfach hintereinander identisch kontextualisierte Prüfung wird nicht ohne Beleg als unabhängig ausgewiesen.

## Hardener-Vertrag

Der Hardener **ändert keinen Plan, keine Definition of Done, keine Architekturentscheidung und keine fachliche Anforderung**. Er erzeugt einen neuen nummerierten Run mit exaktem Quell-/Planstand, Befundliste und Nachweis. Ein Finding enthält ID, Schwere, verletzte Invariante, konkretes Szenario, Expected/Actual, Referenzstellen, Folgen und einen Prüfansatz. Ein Lösungsvorschlag darf hinzugefügt werden, ist aber keine verbindliche Umsetzungsanordnung.

## Befunddisposition

Der Planner bewertet jedes Finding im Gesamtzusammenhang. Zulässige dokumentierte Dispositionen sind: **ACCEPTED_FOR_FIX** (korrekturbedürftig), **ALREADY_COVERED** (mit nachweisbarem Anker bereits abgedeckt), **REJECTED_WITH_REASON** (nichtzutreffend/unverhältnismäßig/gegen übergeordnete Prioritäten), **DEFERRED_BY_APPROVAL** (nur mit ausdrücklich zulässiger, verantworteter Ausnahme) und **BLOCKING** (noch nicht aufgelöst). Widersprüche und hochkritische Befunde führen zu weiteren gezielten Reviews. Eine rein formale Umbenennung eines offenen Pflichtfindings ist keine Schließung.

Entscheidungen über architekturelle Umgestaltung oder erhebliche Risikozugeständnisse erfordern den Auftraggeber. Der Hardener beurteilt keine durch ihn selbst ohne neue Prüfung behobenen Findings als unabhängig bestanden.

## Abschluss-Gate und Freeze

Der Planner integriert alle freigegebenen Korrekturen in Planindex, Verträge, Paketdateien, Traceability, Testplan und Auftragsvorlagen. Der unabhängige Planreviewer prüft den **vollständigen konsolidierten Stand** und die Disposition der früheren Pflichtbefunde. `PLAN_ROOT_PASS` benennt exakt die geprüfte Planbaseline. Anschließend erteilt der Auftraggeber ausdrücklich `PLAN_APPROVED` für Scope, Baseline und Start der Ausführung. Der Planfreeze erzeugt einen eindeutig identifizierten Snapshot/Commit/Tree und einen Freigabenachweis. Ohne gültige Planfreigabe starten keine abhängigen Implementierungspakete.

Später entdeckte Planlücken führen durch Änderungsmanagement zurück zu Planner, erforderlichen Hardening-/Reviewgates und einer neuen, nachweisbaren Baseline; die bereits bestandene Planung wird nicht rückwirkend umgeschrieben.
