# Parameterisierte Auftragsvorlagen

Dateien verwenden `{{VARIABLE}}`-Platzhalter. Der tatsächliche Auftrag muss sämtliche **benötigten** Werte einschließlich Repository, Branch, Paket, Kandidaten-/Baselineidentität sowie Gitrechte aus realen Quellen einsetzen. Ein vorbereiteter Text ist keine bereits erteilte Freigabe.

Verwendung (ohne Netzwerkzugriff):

```powershell
python 03_ANWENDUNGSEBENE/SKRIPTE/render_prompt.py 03_ANWENDUNGSEBENE/PROMPTS/06_REVIEW.md values.json
```

Ein agentischer Folgeauftrag kann kurz bleiben, wenn `dispatcher/SKILL.md` der aktuelle Einstieg ist und der Agent die IDs aus nachgewiesenen Projektakten ermitteln kann. Wer `{{...}}` nicht zuverlässig auflösen kann, stoppt und nennt die fehlende Quelle, statt plausible Werte einzusetzen.
