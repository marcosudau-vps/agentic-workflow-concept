# Paket-, Run-, Status- und Evidenzakten

```text
30_AUSFUEHRUNG/<AP-ID>/
  00_PAKET.md
  01_ENTSCHEIDUNGEN.md           # nur wenn notwendig
  RUNS/
    R01-UMSETZUNG/
      00_PROMPT_ORIGINAL.md
      01_REPORT.md
      EVIDENCE/INDEX.md
      ZUSATZPROMPTS/             # nur bei tatsächlicher Fortsetzung
    R02-ABNAHME/
      00_PROMPT_ORIGINAL.md
      01_REPORT.md
      EVIDENCE/INDEX.md
    R03-KORREKTUR/ ...            # nur wenn Findings existieren
```

Der Status im Paketkopf ist eine dynamische Übersicht; der gültige unabhängige Report ist Quelle des technischen Verdicts. Der menschliche Freigabeoriginalprompt und der echte Merge/Tree-Abschluss sind eigenständige Belege. Der Status des abgeschlossenen Vorgängers kann im nächsten Paket aktualisiert werden, ohne einen zweiten reinen Canonicalizing-Commit zu erzeugen.

`WORKFLOW_STATUS.json` enthält Repo/Zielbranch, Phase, Paketstatus, Auswahl-/Owner-/Berechtigungsquellen, `canonicalParent`, aktuellen Candidate/PR/Run, reviewedCommit/Report, `humanApproval`, offene Finding-IDs, Blocker und genaue nächste Aktion. Planstatus liegt separat in `PLAN_STATUS.json`. Historische Runreports werden nicht überschrieben; die Übersicht darf sich ändern.

Jeder tatsächliche Run enthält nur ein Original, einen Gesamtbericht und einen Evidenzindex als Pflichtdateien. Belege werden einmal abgelegt und anderweitig verlinkt. Tokens, Nutzerinhalt, Audio, private DBs und ungeschwärzte Diagnostik gehören nicht in Git.
