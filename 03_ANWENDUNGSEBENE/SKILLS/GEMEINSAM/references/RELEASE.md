# Releasequalifikation und Veröffentlichung

1. Abgeschlossene Featureaggregate, unabhängige FEATURE_ROOT_PASS-Berichte und ihre expliziten menschlichen Release-Aufnahmefreigaben verifizieren.
2. Exakten Release-Branch-HEAD, Version, geplanten Umfang und verknüpfte Produkte/Serverpaare fixieren.
3. Release-Candidate-Artefakte für jede Pflichtplattform/-edition aus dem eingefrorenen Quellstand bauen. Manifest: Source-SHA/Tree, Build-Toolchain, Dependency Pins, Timestamp, Digest, Artifact und Runtime.
4. Vollständige Matrix pro Build/Install/Smoke/Protokoll/Sicherheit/Migration/Rollout ausfüllen. Nicht gelaufene Plattform als `NOT_RUN` und unbewiesene Herkunft als `NOT_PROVEN` berichten.
5. Unabhängige RC-Qualifikation auf genau diesen Stand. Alte Qualifikation auf anderer SHA nicht fortschreiben.
6. Nach technischer `RELEASE_QUALIFIED` ausdrücklichen menschlichen Auftrag für Main-Aggregation einholen und die Single-Parent-/Tree-/Tag-Identität sichern.
7. Öffentliche Veröffentlichung/Deployment/Registryupload nur nach **separatem** tatsächlichem Auftrag. Zielspeicher, Version, Artefakt-Digest, Credential-/Sicherheitsgrenzen und Nachpublikationschecks kontrollieren.
8. Abschlussstatus kann `RELEASE_QUALIFIED`, `MAIN_ACCEPTED` oder `PUBLISHED` unterscheiden; keines folgt automatisch aus dem anderen.
