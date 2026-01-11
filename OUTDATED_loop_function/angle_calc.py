#requierements for angle_calc:
#gets p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y and calculated angle at p2,p3,p4, no need for full polist calculation
#function is called anglcalc
#and is called with given variables anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y)
#returns list of [angle, angle, angle] fixed length at 3
import math as math
def anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y, itera, isfirst,islast):
    #p3x = 0.5 * (p2x + p4x)
    #p3y = 0.5 * (p2y + p4y)
    altformula = False
    #calculates angle at p2
    ang1 = math.degrees(
        math.atan2(p3y-p2y, p3x-p2x) - math.atan2(p1y-p2y, p1x-p2x))
        #math.atan2(p1y-p2y, p1x-p2x) - math.atan2(p3y-p2y, p3x-p2x))
    #print("orgorgang1", ang1)
    #ang1 = ang1-180
    # if ang1< 0:
    #     altformula = True

    ang1 = (ang1 + 180) % 360 - 180
    ang1 = abs(abs(ang1) - 180)

    #ang1 = abs(ang1 - 180)
    # if ang1 < 0:
    #     ang1 = ang1*-1
    # ang1 = ang1 - 180
    #if -180 > ang1 > 180:
    #    ang1 = ang1 - 360
    # if ang1 < 0:
    #     ang1 = ang1*-1
    #calculates angle at p4
    ang2 = math.degrees(
        math.atan2(p4y-p3y, p4x-p3x) - math.atan2(p2y-p3y, p2x-p3x))
        #math.atan2(p3y-p4y, p3x-p4x) - math.atan2(p5y-p4y, p5x-p4x))
    #print("orgorgang2", ang2)
    #ang2=ang2-180
    # if ang3< 0:
    #     altformula = True

    ang2 = (ang2 + 180) % 360 - 180
    ang2 = abs(abs(ang2) - 180)




    ang3 = math.degrees(
        math.atan2(p5y-p4y, p5x-p4x) - math.atan2(p3y-p4y, p3x-p4x))
        #math.atan2(p3y-p4y, p3x-p4x) - math.atan2(p5y-p4y, p5x-p4x))
    #print("orgorgang3", ang3)
    #ang3=ang3-180
    # if ang3< 0:
    #     altformula = True

    ang3 = (ang3 + 180) % 360 - 180
    ang3 = abs(abs(ang3) - 180)

    #ang3 = abs(ang3 - 180)
    # if ang3 < 0:
    #     ang3 = ang3*-1
    # ang3 = ang3 - 180
    #if -180 > ang3 > 180:
    #    ang3 = ang3 - 360
    #if ang3 < 0:
    #    ang3 = ang3*-1
    # if altang1 < 90 and altang3 < 90:
    #     altformula = True
    # if altang1 > 90 and altang3 < 90:
    #     altformula = True
    # if altang1 < 90 and altang3 > 90:
    #     altformula = True
    # if altang1 > 90 and altang3 > 90:
    #     altformula = False

    #print("more original same angles", ang1,ang2, ang3)
    #return ang1,ang2,ang3

    #all in one solution

    sidesadder=0.4
    exponent=2
    iteraweight=0.1
    #punishment = ang1**(exponent+sidesadder+itera*iteraweight)+ang2**(exponent+itera*iteraweight)+ang3**(exponent+sidesadder+itera*iteraweight)
    
    #punishment = ang1**(exponent+sidesadder/itera+itera*iteraweight)+ang2**(exponent+itera*iteraweight+itera*iteraweight)+ang3**(exponent+sidesadder/itera+itera*iteraweight)

    #punishment = ang1**exponent+((ang2*(0.5+itera*iteraweight))**exponent)+ang3**exponent #alternative with factor 3
    #if itera == 1:
    #    punishment = (ang1**exponent)+((ang2/2)**exponent)+(ang3**exponent) #alternative with factor 3
    #else:
    punishment = (ang1**exponent)+(ang2**exponent)*(itera/2)+(ang3**exponent) #alternative with factor 3
    if isfirst == True:
        punishment = (ang1**exponent)*1.75+(ang2**exponent)*(itera/2)+(ang3**exponent)
    if islast == True:
        punishment = (ang1**exponent)+(ang2**exponent)*(itera/2)+(ang3**exponent)*1.75
    return punishment


#   good results slight overcorrection
#   sidesadder=2
#    exponent=8
#    iteraweight=0.2

