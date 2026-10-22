# Verbindlichkeit, Prüfung, Sicherheit und maschinelle Unterstützung

## Zwei unterschiedliche Autoritätsbereiche

Die allgemeine Konzeptebene beschreibt die **projektübergreifenden Verfahrensregeln**. Die **projektspezifischen Fachentscheidungen** entstehen dagegen innerhalb dieser Regeln durch die zentrale Planung aus Mensch und Planner-Agent. Deren freigegebene Planbaseline macht konkrete Produktanforderungen, Schnittstellenverträge und Abnahmekriterien verbindlich. Die Autoritätsbereiche stehen nicht als konkurrierende Dokumentfassungen nebeneinander: Das Framework regelt, *wie* ein Projekt geplant und seine Ergebnisse verbindlich werden; die zentrale Planung bestimmt, *was* im jeweiligen Projekt gelten soll.

Die Anwendungsebene operationalisiert die Rahmenregeln durch standardisierte Instrumente. Wann ein Instrument zwingend anzuwenden ist und wann es lediglich bedarfsorientiert bereitsteht, ergibt sich aus dem zugehörigen Rollen- oder Gatevertrag. Dokumentinhalt und Freigabestatus einer Fassung werden getrennt behandelt; die neutrale Systembeschreibung enthält keine Entscheidungs- oder Änderungshistorie.

## Regelimplementierung

Die neutralen Systemregeln werden als rollenbezogene Lesepfade, Skills, Vorlagen, Workflowzustände und maschinenlesbare Formate operationalisiert. Jede operative Anweisung muss einer entsprechenden Konzeptregel zugeordnet sein; ein Skill darf keinen neuen Gatezwang oder keine Freigabe durch bloße Existenz erzeugen.

## Deterministische Prüfung

Maschinelle Prüfer validieren Schemas, Pflichtdateien, relative Links, IDs, konsistente aktive Statusfelder, bekannte Zustände, Runreferenzen, Hashformate und deklarierte Nachweisbindungen. Sie bezeugen **Struktur**, nicht fachlichen Inhalt, Runtimewirklichkeit oder menschliche Freigabe. Ihre Resultate sind selbst Evidenz, keine Ersatzautorität.

## Ausführungsgrenzen

Ein automatisierter oder manueller Dispatcher darf einen zulässigen nächsten Auftrag *vorschlagen beziehungsweise nach tatsächlichem Auftrag auswählen*, nicht eigenmächtig alle Folgephasen, Gitaktionen oder Remotezugriffe ausführen. Tooladapter für Codex, Claude Code, Copilot und OpenCode können den bestehenden Rollenvertrag künftig transportieren, ohne die fachlichen Übergangsgates umzudefinieren.

## Informationsschutz

Agenten erhalten nur die für Auftrag und Rolle notwendigen Quellen und Gitrechte. Credentials, Nutzerdaten, Audio, private Diagnosen, Logs mit vertraulichen Inhalten und Tokens bleiben aus offen versionierten Akten ausgeschlossen. Belege werden redigiert oder in vertraglich zulässigen geschützten Speichern mit Checksumme/Locator hinterlegt.

## Konsistenz und Änderung

Eine Regeländerung löst einen Impactcheck auf Konzeptkapitel, Skills, Vorlagen, Schemata, Skripte und Beispiele aus. Noch ungeprüfte Anwendungsvorlagen werden nicht als fertig freigegeben. Der Dokumentstand folgt dem fachlich geprüften Ergebnis, nicht automatisch dem neuesten Zeitstempel.
