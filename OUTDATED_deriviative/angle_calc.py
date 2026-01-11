#requierements for angle_calc:
#gets p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y and calculated angle at p2,p3,p4, no need for full polist calculation
#function is called anglcalc
#and is called with given variables anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y)
#returns list of [angle, angle, angle] fixed length at 3
import math as math
def anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y):
    p3x = 0.5 * (p2x + p4x)
    p3y = 0.5 * (p2y + p4y)
    altformula = False
    #calculates angle at p2
    ang1 = math.degrees(
        math.atan2(p3y-p2y, p3x-p2x) - math.atan2(p1y-p2y, p1x-p2x))
        #math.atan2(p1y-p2y, p1x-p2x) - math.atan2(p3y-p2y, p3x-p2x))
    #print("orgorgang1", ang1)
    if ang1 < 0:
        ang1 = ang1 * -1
        ang1 = ang1 - 180
    elif ang1 >= 0:
        ang1 = ang1 * -1
        ang1 = ang1 + 180
    #ang1 = ang1-180
    #altang1= ang1
    # if ang1< 0:
    #     altformula = True

    #ang1 = (ang1 + 180) % 360 - 180
    #ang1 = (abs(ang1) - 180)

    #ang1 = abs(ang1 - 180)
    # if ang1 < 0:
    #     ang1 = ang1*-1
    # ang1 = ang1 - 180
    #if -180 > ang1 > 180:
    #    ang1 = ang1 - 360
    # if ang1 < 0:
    #     ang1 = ang1*-1
    #calculates angle at p4
    ang3 = math.degrees(
        math.atan2(p5y-p4y, p5x-p4x) - math.atan2(p3y-p4y, p3x-p4x))
        #math.atan2(p3y-p4y, p3x-p4x) - math.atan2(p5y-p4y, p5x-p4x))
    #print("orgorgang3", ang3)
    if ang3 < 0:
        ang3 = ang3 * -1
        ang3 = ang3 - 180
    elif ang3 >= 0:
        ang3 = ang3 * -1
        ang3 = ang3 + 180
    #ang3=ang3-180
    #altang3 = ang3
    # if ang3< 0:
    #     altformula = True

    #ang3 = (ang3 + 180) % 360 - 180
    #ang3 = (abs(ang3) - 180)

    #ang3 = abs(ang3 - 180)
    # if ang3 < 0:
    #     ang3 = ang3*-1
    # ang3 = ang3 - 180
    #if -180 > ang3 > 180:
    #    ang3 = ang3 - 360
    #if ang3 < 0:
    #    ang3 = ang3*-1
    # if altang1 < 0 and altang3 < 0:
    #      altformula = True
    # if altang1 > 0 and altang3 < 0:
    #      altformula = True
    # if altang1 < 0 and altang3 > 0:
    #     altformula = True
    # if altang1 > 0 and altang3 > 0:
    #     altformula = False
    if ang1 < 0 and ang3 < 0:
         altformula = False
    if ang1 > 0 and ang3 < 0:
         altformula = True
    if ang1 < 0 and ang3 > 0:
        altformula = True
    if ang1 > 0 and ang3 > 0:
        altformula = False

    #print("more original same angles", ang1, ang3)
    return ang1, ang3, altformula
