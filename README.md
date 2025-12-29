---USAGE INSTRUCTIONS---

check main for input instructions

check each function for input and return of each

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

---NOTES AND BUGS---

idea: Check nur in die richtung in die Vektoren Zeigen (siehe GGB)
bug: x1 and x2 cannot be the same and also most other imput x/y


---FUNCTION STATUS---

main.py
 finished
plotter.py
 finished
pointinserter.py
 unstable version finished
angle_calc.py
 not started
angle_punishment.py
 not started




