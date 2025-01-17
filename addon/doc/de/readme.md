# Spalten-Betrachter #

* Autoren: Alberto Buffolino, Łukasz Golonka, andere Entwickler
* [Stabile Version herunterladen][stable]
* [Entwicklerversion herunterladen][dev]
* NVDA-Kompatibilität: 2017.3 und neuer

Spaltenbetrachter ist eine Erweiterung zur Verbesserung der NVDA-Erfahrung
mit Listen.

Zu den Funktionen gehören:

* anpassbare Aktionen für Spaltenüberschriften und/oder -Inhalt (verfügbare
  Aktionen sind Lesen, Kopieren, Buchstabieren und Anzeigen im Lesemodus);
* Fähigkeit, zwischen Spalten in Zehn-bis-Zehn-Intervallen zu wechseln;
* Vereinfachte Überschriften-Verwaltung (Maus-Klicks);
* Ausgabe der aktuellen Positionsinformation bei Bedarf (bspw. Eintrag 7 von
  10)
* anpassbare Gesten mit oder ohne Nummernblock;
* Die Ansage "0 Einträge", wenn die Liste lehr ist (derzeit nicht in Windows
  8/10-Ordnern)
* Unterstützung für alles lesen;
* Ansage der markierten Einträge (Anzahl und Namen der Einträge);
* Listensuche (mit Mehrfachauswahl von Listeneinträgen, falls
  angehakt/unterstützt).

## Gesten

Die Standard-Tastenkombinationen für Spalten, Überschriften und Position
beinhalten NVDA+Steuerung. Dies kann in den Erweiterungseinstellungen, (aber
nicht in den "Tastenbefehlen") geändert werden.

Beachten Sie, dass Ihre Tastatur Probleme bei der Verarbeitung einiger
Tastenkombinationen haben könnte. Probieren Sie daher alle zusätzlichen
Gesten aus und passen Sie diese für bessere Ergebnisse an.

Siehe auch die Erweiterungs-Einstellungen für den Nummernblock-Modus,
Tastaturschema (ohne Nummernblock) und die vier verfügbaren Aktionen für
Spalten.

* NVDA+Steuerung+Ziffern von 1 bis 0 (Tastaturmodus) oder von 1 bis 9
  (Nummernblockmodus): einmal drücken: die ausgewählte Spalte wird
  vorgelesen; zweimal drücken: die Spalte wird in die Zwischenablage
  kopiert;
* NVDA+Steuerung+nummernblock Minus (Nummernblockmodus): wie
  NVDA+Steuerung+0 im Tastatur-Modus, Lesen oder Kopieren der 10ten, 20ten
  Spalte usw.;
* NVDA+Steuerung+- (Tastaturmodus, Layout EN-US): Ändern Sie in einer Liste
  mit mehr als 10 Spalten das Interwall und greifen so auf die Spalten
  11-20, 21-30, usw. zu. Ändern Sie das letzte Zeichen in den Einstellungen
  passend zu Ihrem Tastaturschema;
* NVDA+Steuerung+nummernblock Plus (Nummernblockmodus): genau wie beim
  vorherigen Befehl nur rückwärts;
* NVDA+Steuerung+Eingabe (nummernblock Eingabe im Nummernblockmodus):
  Spaltenüberschriften-Manager öffnen;
* NVDA+Steuerung+entfernen (Nummernblock entfernen im Nummernblock-Modus):
  Lese die aktuelle sowie die relative  Position des Listeneintrags,
  bspw. Eintrag 7 von 10;
* Pfeiltasten und NVDA+tab (in einer leeren Liste): Nachricht "0 Elemente"
  wird wiederholt;
* NVDA+Pfeil nach unten (Desktop-Schema) oder NVDA+a (Laptop-Schema):
  Startet alles lesen (diese Geste hängt von der Belegung der
  "Tastenbefehle" Kategorie „Systemcursor“ ab);
* NVDA+Umschalt+Pfeil nach oben (Desktop-Schema) oder NVDA+Umschalt+s
  (Laptop-Schema): Sagt die Anzahl und die Namen der ausgewählten
  Listeneinträge an (wie der vorherige Befehl zur Anpassung);
* NVDA+Strg+F: Suchdialog öffnen (nicht anpassbar);
* NVDA+f3: Nächstes Vorkommen von zuvor eingegebenem Text finden (nicht
  anpassbar);
* NVDA+Umschalt+f3: suche vorheriges vorkommen (nicht veränderbar).

## Unterstützung

Diese Erweiterung bietet eine allgemeine Unterstützung für häufigere Listen
(siehe unten) und einige spezifische Anwendungen. Der Hauptautor (Alberto
Buffolino) kann die Kompatibilität/Funktionalität für nicht verwendete
Anwendungen wie  Outlook und Windows Mail nicht garantieren. Er wird gerne
mit ihren Benutzern zusammenarbeiten oder einen Pull Request für die
Anwendungen annehmen.

Unterstützte Listen sind:

* SysListView32;
* DirectUIHWND (in 64-Bit-Systemen vorhanden);
* WindowsForms10.SysListView32.* (Anwendungen, die .NET verwenden);
* mehrspaltige Baumansicht wie in RSSOwlnix;
* Mozilla-Tabelle (typischerweise Thunderbird-Nachrichtenliste, gruppierte
  Beiträge werden unterstützt).


[[!tag dev stable]]


[stable]: https://addons.nvda-project.org/files/get.php?file=cr

[dev]: https://addons.nvda-project.org/files/get.php?file=cr-dev
