from angle_calc import anglcalc
from angle_punishment import anglepunishment
import math as math

def spawner(polist, itera):
    rangesetter = len(polist[0])-1
    i=0
    while i < rangesetter:
        if(i != 0 and i != rangesetter-1 and i != rangesetter): #check if point has to be created (dont create point if in start vectors)

            #define points used for angle calculation
            p1x = float(polist[0][i-1])
            p1y = float(polist[1][i-1])
            #if(i>1): #funky alternative version that overcorrects + bug but is symmetrical
            #   p1x = float(polist[0][i-2])
            #   p1y = float(polist[1][i-2])
            p2x = float(polist[0][i])
            p2y = float(polist[1][i])
            p3x = float(float(polist[0][i]+polist[0][i+1])/2) #this defines the new current points x
            p3y = float(float(polist[1][i]+polist[1][i+1])/2) #this defines the new current points y
            p4x = float(polist[0][i+1])
            p4y = float(polist[1][i+1]) 
            p5x = float(polist[0][i+2])
            p5y = float(polist[1][i+2]) 
            
            #define deltax and deltay of right triangle between p2, p3, finalp
            deltax = p3x - p2x
            deltay = p3y - p2y

            #calculates two angles with given points
            ang1, ang3 = (anglcalc(p1x,p1y,p2x,p2y,p4x,p4y,p5x,p5y))

            ang2 = anglepunishment(ang1,ang3,i,rangesetter, itera)

            #define oldang1 for formula
            oldang1 = ang1

            #update ang1 based on relation with ang2 (Gleichschenkliges Dreieck Winkel) (ang3 doesnt need to be updated using ang3-ang2/2 because it is no longer used)
            ang1=ang1-ang2/2
            
            #define usedang1 for formula as diffrence between oldang1 ang ang1
            usedang1 = oldang1-ang1
            
            #variant that combines above lines into one
            #usedang1 = ang1-ang1-ang2/2

            #formula that works on everything now
            finalx = (p2x+deltax-math.tan(usedang1*math.pi/180)*deltay)
            finaly = (p2y+deltay+math.tan(usedang1*math.pi/180)*deltax)

            #formula for going right of line
            #if altformula == True:
            #    finalx = (p2x+deltax+math.tan(usedang1*math.pi/180)*deltay)
            #    finaly = (p2y+deltay-math.tan(usedang1*math.pi/180)*deltax)
            
            #insert final point into polist
            polist[0].insert(i+1,(finalx))
            polist[1].insert(i+1,(finaly))

            #add an extra iteration and rangesetter because point has been added
            i=i+1
            rangesetter = rangesetter + 1
        i=i+1

    return polist

