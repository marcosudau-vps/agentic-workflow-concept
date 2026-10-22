# Einsetzbare Projektstruktur

Im Zielprojekt wird ein eigener Arbeitsblock (hier beispielhaft `ARBEITSPROZESS/`) erstellt. Die folgenden Bezeichnungen sind für das hier beschriebene **Initialmodell** stabil. Der Projektname, konkrete Git-Branches, Zielsysteme und Requirements sind konfigurationsbezogen zu ergänzen. Unterordner für künftige Korrektur-/Reviewruns werden **nicht** im Voraus vorproduziert.

```text
<ZIELREPO>/
  AGENTS.md                        # projektbezogene Einstiegspfade und Rangfolge
  ARBEITSPROZESS/
    README.md                      # aktives Vorhaben, Plan-/Status-/Skills-Einstieg
    TRACKING/
      WORKFLOW_STATUS.json         # aktive ausführungsbezogene Statusübersicht
      FEATURE_STATUS.json          # unabhängige Featuregesamtprüfung und Releaseaufnahme
      STATUS.md                    # aktuelle menschliche Übersicht
      VERLAUF.md                   # append-only Meilensteine
    20_PLANUNG/
      PLAN_STATUS.json             # Phase, Baseline, Hardening-/Reviewstatus
      00_PLANINDEX.md
      ZIELBILD.md
      IST_BASELINES.md
      ARCHITEKTUR.md
      RISIKEN_UND_ENTSCHEIDUNGEN.md
      VERTRAEGE/
      TRACEABILITY/requirements.json
      TRACEABILITY/TRACEABILITY_MATRIX.md
      TEST_UND_ABNAHMEPLAN.md
      EVIDENCE/package-manifest.json
      FEATURES/<FEATURE-ID>.md
      ARBEITSPAKETE/<AP-ID>.md
      RUNS/Rnn-<PLANROLLE>/        # erst bei tatsächlichem Plan-/Hardening-Run
    30_AUSFUEHRUNG/
      <AP-ID>/
        00_PAKET.md
        RUNS/Rnn-<ROLLE>/           # erst je tatsächlich ausgeführtem Run
    40_RELEASE/
      <VERSION>/
        00_RELEASE.md
        RC_MATRIX.json
        RUNS/Rnn-QUALIFIKATION/
    SKILLS/                        # tatsächlich eingesetzte Rolle-/Gemeinsam-Skills
    SCRIPTS/                       # tatsächlich eingesetzte Prüf-/Promptskripte
```

## Zuordnung zu den Vorlagen

Die [Vorlagenbibliothek](../VORLAGEN/README.md) enthält projektneutrale Ausgabestände für alle wiederkehrenden Akten. Sie wird anhand des Projekts konkretisiert. Rollenpfade in den Skills sind **relativ zum `SKILLS/`-Ordner** auflösbar; bei Übernahme ohne die gemeinsame Skillhierarchie müssen entsprechende Pfade angepasst werden.

## Git-Integration

Für die komplexe Ausgangskonstellation existieren separate Release-, Feature- und Paketlinien. `main` bleibt auf geprüfte Gesamt-Releases beschränkt. Planstart/Planfreeze ist ein identifizierter Feature-/Planstand. Eine aktuelle Statuskopie auf einem Integrationsbranch darf bei aktiver Paketarbeit veraltet sein; offene PR-Headakten haben dann Vorrang. Die übrigen Rollen- und Gategrenzen sind in den Skills beschrieben.
