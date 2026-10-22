# Git-Start – Windows / PowerShell

Das ZIP enthält **keinen** `.git`-Ordner; es ist ein Verzeichnisbaum für den Erstimport. Zielrepository: `agentic-workflow-concept`. Keine automatischen Netzwerkänderungen durch das Archiv.

## Das Repository und der Arbeitsbranch sind bereits angelegt

```powershell
gh repo clone <OWNER>/agentic-workflow-concept
cd agentic-workflow-concept
git switch work/gesamtkonzept-v1
# Jetzt den INHALT des gelieferten Projektordners hier hinein kopieren (vorhandene README bewusst ersetzen).
python 03_ANWENDUNGSEBENE/SKRIPTE/check_repository.py
python -m unittest discover -s tests -v
git status --short
git add .
git commit -m "docs: initialer agentic-workflow Gesamtgrundstand"
git push -u origin work/gesamtkonzept-v1
```

Alternativ nach `git clone` die PowerShell-/Git-Befehle ohne `gh` verwenden. Falls das Repository **leer** ist, kann der erste Push zunächst `work/gesamtkonzept-v1` erzeugen; GitHub braucht ggf. einen separat erzeugten minimalen `main`, bevor der Entwicklungsbranch später per PR in ihn gemergt werden kann. Ein noch nicht vorhandenes `main` nicht mit der unfertigen Gesamtfassung initialisieren, wenn `main` nur vollständige Fassungen enthalten soll.

Vor dem späteren Merge nach `main`: gegenseitige Konzept-/Anwendungskonsistenz, Quellen-/Entscheidungsbelege, Tests, Gesamtprüfung und ausdrückliche menschliche Freigabe. Weder der Initialcommit noch die hier verwendete Branchbezeichnung ist eine Freigabe des Fachkonzepts.
