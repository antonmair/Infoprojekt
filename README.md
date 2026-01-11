---WHAT IS IT---

An algorithm that creates a path in between two vectors, trying to make it as smooth as possible


---USAGE INSTRUCTIONS---

Run _main.py, input 4 points, the first point defines the start of vector 1 the second point defines the end of vector 1, the third point defines the start of vector 2 and the fourth the end of vector 2

IMPORTANT: The line will be drawn from end of vector 1 (point2), towards start of vector 2 (point3), point 1 and 4 determine the direction that the curve will try to smooth towards.

---CONCEPT---

Ein Algorithmus, der Anhand von zwei gegebenen Punkten, die jeweils in eine Richtung Zeigen, eine möglichst kurvenoptimale Trasse Findet (mit verwendung von der Abweichung von 180 Grad an Punkt). 
Erweiterung möglich wo Objekte aus OSM Objekten (z.B. Häuser) bestehen und so eine reale Trassenplanung möglich ist. 

An algorithm that with four given points defining two vectors, finds the optimal right of way. Furthermore: possibly adding OSM Objects (e.g. Houses) for further planning ability, taking houses into consideration.

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
 finished

---CREDITS---

 Anton Mair [Mat. Nr. 102964]
 
 Ava Ditkun [Mat. Nr. 102253]
