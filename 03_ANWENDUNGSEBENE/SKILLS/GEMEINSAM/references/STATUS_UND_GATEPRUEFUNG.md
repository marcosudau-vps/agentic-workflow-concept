# Status und Gateprüfung

## Lesereihenfolge

1. Offene, dem Projekt zugeordnete Paket-/Feature-/Fix-PRs auf ihren tatsächlichen Zielzweig prüfen.
2. Ausgewählte Kandidatenbranche und deren versionierten `WORKFLOW_STATUS.json` lesen. Der abgeschlossene Integrationsbranch enthält laufende Arbeit regelmäßig nicht.
3. Runakte, `00_PAKET.md`, Manifest, `writeOwner`, Reviews, Freigabeoriginale und Git-/PR-Commits gegeneinander prüfen.
4. Konkurrenzen/fehlende Berechtigungen/unerreichbare WIP ausdrücklich markieren.
5. **Genau eine** nächste fachlich erlaubte Aktion auswählen und deren Rolle/Lesepfad nennen.

## Typische Zuweisungen

| Beleglage | Nächste zulässige Aktion |
| --- | --- |
| Plan erstellt / qualifizierte Härtung nötig | Hardener mit exakt eingefrorenem Plan-SHA |
| Offene Härtungsfindings | Plannerdisposition, gegebenenfalls Revision |
| Vollständiger Planreview-PASS ohne menschliche Planfreigabe | Warten/Planfreigabe erbitten |
| `PLAN_APPROVED`, AP ready, Vorgänger nachweislich übernommen | Implementer |
| `REVIEW_READY` und keine aktive fremde Review-Schreibhoheit | frischer Technical Reviewer |
| `CHANGES_REQUIRED` | Implementer-Korrekturlauf nach Review-Docs-Übernahme |
| `ROOT_PASS` ohne Übernahmeprompt | Warten und dem Menschen PASS/Scope erläutern |
| ausdrücklicher Übernahmeprompt + PASS + qualifizierte Head/Base/CI | Canonicalizer |
| aktive fremde Schreibhoheit / Konflikt | nur dokumentierte Recovery oder Blockermeldung |
| anerkannter Crossrepo-Blocker | gesonderten autorisierten FIX verfolgen |
| alle APs vollständig angenommen, Featuregesamtstand bereit | unabhängiger Feature Qualifier |
| gültiger FEATURE_ROOT_PASS, keine Featurefreigabe | Warten auf menschliche Release-Aufnahmefreigabe |
| alle Featureaggregate und RC-Matrix bereit | Release Qualifier / menschliche Releaseentscheidung |

**Kein Statuswert allein beweist einen Übergang.** Test- und Freigabequellen zuerst verifizieren.
