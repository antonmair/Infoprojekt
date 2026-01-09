import math as math

def anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y):
    #p3x = 0.5 * (p2x + p4x)
    #p3y = 0.5 * (p2y + p4y)
    altformula = False
    
    #calculates angle at p2
    ang1 = math.degrees(
        math.atan2(p3y-p2y, p3x-p2x) - math.atan2(p1y-p2y, p1x-p2x))#p3 is redundant could be replaced with p2/4
    #print("orgorgang1", ang1)
    if ang1 < 0:
        ang1 = ang1 * -1
        ang1 = ang1 - 180
    elif ang1 >= 0:
        ang1 = ang1 * -1
        ang1 = ang1 + 180


    #calculates angle at p4
    ang3 = math.degrees(
        math.atan2(p5y-p4y, p5x-p4x) - math.atan2(p3y-p4y, p3x-p4x))
    #print("orgorgang3", ang3)
    if ang3 < 0:
        ang3 = ang3 * -1
        ang3 = ang3 - 180
    elif ang3 >= 0:
        ang3 = ang3 * -1
        ang3 = ang3 + 180


    #quadrant thingy
    if ang1 < 0 and ang3 < 0:
         altformula = False
    if ang1 > 0 and ang3 < 0:
         altformula = True
    if ang1 < 0 and ang3 > 0:
        altformula = True
    if ang1 > 0 and ang3 > 0:
        altformula = False

    return ang1, ang3, altformula

