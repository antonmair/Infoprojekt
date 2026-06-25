Öffnung des Programmes:

package Install

pip install jupyterlab ipyleaflet numpy geopandas scipy osmnx geopy voila


jupyter lab

Windows:
In jupiternotebook:

cd "C:\Users\"path"\Infoprojekt_main"

python -m jupyterlab 


In voila (ipnyb output als eigene Seite):

cd "C:\Users\"path"\Infoprojekt_main"

python -m voila jupiterpython.ipynb


Mac (python oder python3)

In jupiternotebook:

cd "/Users/"path"/Infoprojekt_main

python -m jupyterlab

In voila

cd "/Users/"path"/Infoprojekt_main

python -m voila jupiterpython.ipynb


Aktivierung in jupiternotebook:

run jupiterpython.ipnyb



Verwendung des Programmes:

Das Programm ist ein algorithmischer Trassenplanner. Für die Erstellung einer Klasse mussen 4 Klicks auf die Kartenoberfläche eingegeben werden. 

Die Orte dieser 4 Punkte beschreiben wie folgt die Trasse:

  1. zu 2. Click: Richtung/Orientierung der Trasse am Anfang
     
  3. Click: Start der Trasse
     
  5. Click: Ende der Trasse
     
  3. zu 4. Click: Richtung/Orientierung der Trasse am Ende

     

Parametrisierung:

  Haussuchradius: Kreis der den Bereich des geladenen OSM Bereiches darstellt
  
  Winkelkurve: Geometrische Winkelkurve, die auf der Kurve des Vorgängerprojektes aufbaut, die aber jetzt schneller und genauer ist
  
  Iterationen zeigen: Wenn diese Option aktiviert ist, wird die Trasse (Haustrasse) bereits während dem Algorithmus dargestellt und die geographische endwicklung der Trasse ist über die Iterationen einsehbar, wenn diese Option deaktiviert wird, wird die Trasse erst im Nachinein angezeigt.
  
  Haltepunkte generieren: Haltepunkte werden generiert, kann etwas länger dauern
  

Der Algorithmus funktioniert Prinzipiell durch eine Bewertung von den Faktoren: Nähe zu Bebauung und geometrische Direktheit. Anhand von Diesen Faktoren wreden im gewählten Bereich, k Iterationen wiederholt, Mittelpunkte erstellt die an einer Normalen zu dem mathematischen Minimum verschoben werden. Dieses beachtet die Faktoren und kann wie wie folgt manipuliert werden:
Die Checkboxes erlauben es verschiedene optionale Elemente ein und aus zu schalten, dazu gehören:

  Direktheit: Umso höher der Direktheit Wert ist, desto weniger verschwenkt ist die Trasse und, desto mehr ähnelt sie sich der blauen Winkelkurve, dieser Wert kann auch durch manuelle Eingabe über das Slider Limit gesetzt werden, wenn eine direktere Trasse erwünscht ist.
  
  Hausscheue: Umso höher dieser Wert ist, desto mehr entfernt sich die Trasse von Siedlungen, dieser Wert kann auch durch manuelle Eingabe über das Slider Limit gesetzt werden
  
  Erschließung: Umso höher dieser Wert ist, desto mehr probiert das Programm Siedlungen Anzuschließen. Dieser Wert kann gegensätzlich zu Hausscheue funktionieren, hat aber im Algorithmus den Unterschied, dass wenn z.B. beide Slider hohe Werte haben, die Erschließung trotzdem eher versucht nahe gelegene (ca.500m) Siedlungen zu erschließen, es kann aber auch bei hohen Erschließungswerten durchaus vorkommen das durch Siedlungen Trassiert wird.


Hinweise und Trassenartenvorschläge:

  Bei nähe zu Großstädten (wo diese auch größtenteils im Ladebereich sind) sollte der Erschließungsslider tendenziell stark runtergestuft werden, da der Algorithmus sonst zu Weit in Richtung Stadtmitte gezogen wird.

  In Gebieten wo OSM Gebäude nicht konsequent und flächendeckend gemappt sind funktioniert der Algorithmus nur fehlerhaft/nicht.

  Für lokalere Bahnen muss der direktheisfaktor Tendenziell sehr niedrig sein (<50), außer die anderen Parameter sind auch sehr niedrig.

  Der dritte Slider geht nicht aus den boundaries 0-2000 raus, da die logik 2001-n ist. Das führt auch dazu das bei Werte nahe 2000 die änderungen auch bei geringerer Verschiebung größer sind als anderswo.

  Das Projekt ist auch prinzipiell nicht für urbane Trassen wie Straßenbahnen geeignet. Außer man Interpretiert es als U-Bahn

  Bahnarten:

  2000, 4600, 700 (Hochgeschwindigkeitsstrecke mit Feldbahnhöfen)
  
  500, 10000,500 (eher langsamer Fernverkehr mit wenig Störung in Siedlungsbereichen, Güterbahntrasse)
  
  860,5320,1400 (schneller Regionalverkehr mit am Ortsrand gelegenen Bahnhöfen)
  
  50, 1000, 500 (langsamerer Regionalverkehr mit Lokalanschließung)
  
  1, 500, 1900 (langsame Lokalbahn mit Starker anschließung (z.B. Stubaitalbahn)

  50,0,2000 (U-Bahn)

Die Speicherung von Hausdaten als cache greift auf den lokalen Speicherplatz zurück weshalb nach Verwendung die Hausdaten gespeichert bleiben und endsprechend auch viel Speicherplatz einnehmen können.
  
  
  

  


