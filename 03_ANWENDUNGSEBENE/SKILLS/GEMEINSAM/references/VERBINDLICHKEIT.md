# Verbindlichkeit – operative Auslegung

| Kennzeichnung | Beispiel | Behandlung |
| --- | --- | --- |
| `V1_CONTRACT` | Wire-/Persistenzformat, Authentisierung, API-Felder | Exakt; Änderungsantrag mit Planfreigabe |
| `V2_OUTCOME` | keine doppelte Ausgabe, sichere Migration, PASS-Gate | Wirkung und Pflichtnachweis zwingend; interne Implementation frei |
| `V3_SUGGESTION` | Dateinamen, interne Klassen, Callbackform | Alternative bei nachgewiesener Äquivalenz zulässig; kurz erläutern |
| `V4_START_VALUE` | Queue-/Timeoutgrenze | anhand reproduzierbarer Tests/Messung ändern; tatsächlichen Wert dokumentieren |

Hardener und Reviewer bewerten **verletzte Wirkungen**, nicht vorgeschlagene Modulnamen. Eine andere Klassennamenswahl ist allein kein Pflichtfinding. Keine Umdeutung eines tatsächlichen Schnittstellenwerts zum technischen Startwert. Umsetzungsagenten ändern keine Produktgrenzen, Verträge, Datenschutz- oder Abnahmeansprüche stillschweigend.
