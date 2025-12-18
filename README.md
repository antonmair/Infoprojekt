Ein Algorithmus, der Anhand von zwei gegebenen Punkten, die jeweils in eine Richtung Zeigen, eine Trasse findet, die dynamisch Anhand der Faktoren Distanz, 
Entfernung zu Objekten und Kurvenradius (oder abweichung von 180 Grad an Punkt), eine Trasse findet, die  nach angegebenen Parametern die vorteilhafteste ist. 
Erweiterung möglich wo Objekte aus OSM Objekten (z.B. Häuser) bestehen und so eine reale Trassenplanung möglich ist. 

Einheiten sollten Meter endsprechen, alle 10 Meter ein Penaltycheck
Feature List

Base:
Splitting Algorithmus
Penalty Calc (Angles)

Extra:
Obstacles
Penalty Calc (Obstacles)

Extra Extra:
OSM Objects

Überlegungen Algorithmus
Check nur in die richtung in die Vektoren Zeigen (siehe GGB)
