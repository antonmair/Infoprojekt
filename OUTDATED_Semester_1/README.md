---WHAT IS IT---

An algorithm that creates a path in between two vectors, trying to make it as smooth as possible


---USAGE INSTRUCTIONS---

Run _main.py, input 4 points, the first point defines the start of vector 1 the second point defines the end of vector 1, the third point defines the start of vector 2 and the fourth the end of vector 2

IMPORTANT: The line will be drawn from end of vector 1 (point2), towards start of vector 2 (point3), point 1 and 4 determine the direction that the curve will try to smooth towards.

The sliders can be changed and will change the way the line looks / is optimised

The worsening prohibitator is diabled by default. This setting will create more straight lines within the path and prevents some overcorrect issues. This will howerer mean that curves are usually tighther

The side multiplier defines how much more the side angles are punished. A high value makes the angles directly ajesant to the vectore smoother but will lead to some questionalbe pathfinding on some examples. A low value means side angles are not punished as severly which often leads to straighter, more direct paths at the cost of a smoth entry and exit

The iterations slider defines the amount of iterations the code runs. This defines the amount of times new points are inserted inbetween every point of previos iterations. The iterations visualizer only visualizes up to 6 iterations because further changes are not as visible. The final line will however be the result of all the chosen iterations.

The files in the Folders are other version with some diffrent calculation methods for punishment and also the older loop version, these are used for debugging and optimizing of the formula

---CONCEPT---

An algorithm that with four given points defining two vectors, finds the optimal right of way (calculating offset to 180° on all given points, iterating twelve times, each iteration adding a newly set point and recalculating the offset).


---FUNCTION STATUS---

main.py
 [finished]

plotter.py
 [finished]
 
pointinserter.py
 [finished]
 
angle_calc.py
 [finished]
 
angle_punishment.py
 [finished]
 

---POSSIBLE DEVELOPMENTS---

Add OSM Objects (e.g. Houses)


---CREDITS---

 Anton Mair [Mat. Nr. 102964]
 
 Ava Ditkun [Mat. Nr. 102253]
