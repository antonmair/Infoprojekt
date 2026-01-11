---USAGE INSTRUCTIONS---

check main for input instructions

check each function for input and return of each

See main.py for program, start it and use the mouse cursor to set 4 points 

---KONZEPT---

Ein Algorithmus, der Anhand von zwei gegebenen Punkten, die jeweils in eine Richtung Zeigen, eine Trasse findet, die dynamisch Anhand der Faktoren Distanz, 
Entfernung zu Objekten und Kurvenradius (oder abweichung von 180 Grad an Punkt), eine Trasse findet, die  nach angegebenen Parametern die vorteilhafteste ist. 
Erweiterung möglich wo Objekte aus OSM Objekten (z.B. Häuser) bestehen und so eine reale Trassenplanung möglich ist. 

Einheiten sollten Meter entsprechen, alle 10 Meter ein Penaltycheck

Für die Vorgehensweise siehe "Definitions"

---FEATURE LIST---

-Base:
Splitting Algorithmus
Penalty Calc (Angles)

-Extra:
Obstacles
Penalty Calc (Obstacles)

-Extra Extra:
OSM Objects

---ALT VERSION---
using math function currently not online and without loops, much faster but not as easily moddable und thus worse results but more potential

---NOTES AND BUGS---

idea: Check nur in die richtung in die Vektoren Zeigen (siehe GGB)
idea: use function to find localmin of the following angle function (a - x / 2)² + x² + (b - x / 2)² where a is the first static angle x is the second movable angle and b is the third static angle (would need scraping of entire original algorithm)

---FUNCTION STATUS---

main.py
 finished
plotter.py
 finished
pointinserter.py
 finished
angle_calc.py
 finished
angle_punishment.py
 removed

---CREDITS---

 Anton Mair [Mat. Nr. 102964]
 
 Ava Ditkun [Mat. Nr. 102253]
