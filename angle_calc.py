import math as math
def anglcalc(p1x,p1y,p2x,p2y,p4x,p4y,p5x,p5y):
    
    #calculates angle at p2
    ang1 = math.degrees(
        math.atan2(p4y-p2y, p4x-p2x) - math.atan2(p1y-p2y, p1x-p2x))
    if ang1 < 0:
        ang1 = ang1 * -1
        ang1 = ang1 - 180
    elif ang1 >= 0:
        ang1 = ang1 * -1
        ang1 = ang1 + 180

    #calculates angle at p4
    ang3 = math.degrees(
        math.atan2(p5y-p4y, p5x-p4x) - math.atan2(p2y-p4y, p2x-p4x))
    if ang3 < 0:
        ang3 = ang3 * -1
        ang3 = ang3 - 180
    elif ang3 >= 0:
        ang3 = ang3 * -1
        ang3 = ang3 + 180

    #quadrant problem thingy (no more)
    
    return ang1, ang3
