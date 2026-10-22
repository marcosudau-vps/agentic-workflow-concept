# Lokale Hilfswerkzeuge

Alle Werkzeuge sind offline und benötigen nur die Python-Standardbibliothek. Sie üben keine Netzwerk-/Git-/Merge-/Releaseaktion aus.

```powershell
python 03_ANWENDUNGSEBENE/SKRIPTE/check_repository.py
python 03_ANWENDUNGSEBENE/SKRIPTE/check_project_records.py --project <ZIELREPO>/ARBEITSPROZESS
python 03_ANWENDUNGSEBENE/SKRIPTE/render_prompt.py 03_ANWENDUNGSEBENE/PROMPTS/07_REVIEW.md values.json
```

- `check_repository.py`: interne Markdown-Dateilinks, JSONsyntax, Quellenintegrität und Konzept-zu-Anwendung-Zuordnung (Strukturprüfung).
- `check_project_records.py`: reale Plan-/Workflow-/Requirements-/Manifest-Grundfelder und referenzierte aktive Statusidentitäten. **Keine fachliche Gate-Freigabe**.
- `render_prompt.py`: strikt befüllte `{{NAME}}`-Prompts generieren; unbelegte Variablen führen zu Fehler; Ausgabe auf stdout ohne Sessionstart.

Für externe Branch-/PR-/CI-/Plattform-Identitäten ist ein realer Agenten-/Toolzugriff nötig; diese Werkzeuge behaupten ihn nicht.
