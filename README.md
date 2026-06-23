Öffnung des Programmes:

Windows:
In jupiternotebook:
cd "C:\Users\anton\Desktop\Curve\jupiterprojectcosetta"
python -m jupyterlab 

In voila (ipnyb output als eigene Seite):
cd "C:\Users\anton\Desktop\Curve\jupiterprojectcosetta"
python -m voila jupiterpython.ipynb

Mac
In jupiternotebook:
cd "/Users/"path"/"projektordner"
python -m jupyterlab

In voila (ipnyb output als eigene Seite):
cd "/Users/"path"/"projektordner"
python -m voila jupiterpython.ipynb

Verwendung des Programmes:
Das Programm ist ein algorithmischer Trassenplanner. Für die Erstellung einer Klasse mussen 4 Klicks auf die Kartenoberfläche eingegeben werden. 
Die Orte dieser 4 Punkte beschreiben wie folgt die Trasse:
  1. zu 2. Click: Richtung/Orientierung der Trasse am Anfang
  2. Click: Start der Trasse
  3. Click: Ende der Trasse
  3. zu 4. Click: Richtung/Orientierung der Trasse am Ende

Parametrisierung:
Die Checkboxes erlauben es verschiedene optionale Elemente ein und aus zu schalten, dazu gehören:
  Haussuchradius: Kreis der den Bereich des geladenen OSM Bereiches darstellt
  Winkelkurve: Geometrische Winkelkurve, die auf der Kurve des Vorgängerprojektes aufbaut, die aber jetzt schneller und genauer ist
  Iterationen zeigen: Wenn diese Option aktiviert ist, wird die Trasse (Haustrasse) bereits während dem Algorithmus dargestellt und die geographische endwicklung der Trasse ist über die Iterationen einsehbar, wenn diese Option deaktiviert wird, wird die Trasse erst im Nachinein angezeigt.
  Haltepunkte generieren: Haltepunkte werden generiert, kann etwas länger dauern

  Direktheit: Umso höher der Direktheit Wert ist, desto weniger verschwenkt ist die Trasse und, desto mehr ähnelt sie sich der blauen Winkelkurve, dieser Wert kann auch durch manuelle Eingabe über das Slider Limit gesetzt werden, wenn eine direktere Trasse erwünscht ist.
  Hausscheue:
  Erschließung:


Hinweise und Trassenartenvorschläge:
  Bei nähe zu Großstädten (wo diese auch größtenteils im Ladebereich sind) sollte
  
  
  

  


