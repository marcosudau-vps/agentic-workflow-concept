# Kanonische Übernahme – Preflight und Postflight

**Nur nach tatsächlich erteilter ausdrücklicher menschlicher Übernahmefreigabe.**

1. Originalwortlaut erhalten; PR, freigegebener Head, Tree, canonicalParent und PASS-Report eindeutig auflösen.
2. PR-Base/Head und Ziel-HEAD unmittelbar vor Merge erneut prüfen; Reviewer-SHA/Tree und gültige Kontrakt-/Crossrepo-Baselines verifizieren.
3. Diff seit geprüftem Kandidaten auf ausschließlich erlaubte administrative Änderungen prüfen, einschließlich etwaigem Freigabe-Sicherungscommit.
4. Finale erforderliche CI auf aktuellem Head bzw. unverändertem Head/Base-Testmerge, Mergeability und alle Pflichtchecks prüfen.
5. Genau einen explizit genehmigten Squash- oder vorbereiteten Single-Parent-Aggregationsweg ausführen; nicht beide, nicht autoveröffentlichen.
6. Nach Merge tatsächlichen Aggregate-SHA aus Git lesen: `parent_count==1`, `parent==canonicalParent`, `count(parent..aggregate)==1`, `tree==autorisierter finaler Head-Tree`.
7. Wirklichen PR-/Transportabschluss, Freigabeoriginal, Reviewidentität, CI und Aggregatecommit melden. Unvollständiger Merge ist kein `ACCEPTED`.
8. Nachmerge-SHA in der nächsten Paketakte oder separatem Abschlussnachweis aufnehmen, nicht als Selbstreferenz in einen noch nicht existierenden Mergecommit schreiben.

Release-/Main-Promotion, Tag, externe Publikation, Deployment und Branchcleanup werden nicht implizit erteilt.
