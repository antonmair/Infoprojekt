def anglepunishment(ang1, ang3, i, rangesetter, itera, side, wtol):
        #main function based on 2 as exponent
        ang2 = ((ang1+ang3)/3) 

        #special cases for corners
        if i == 1:
           ang2 = ((ang1*side+ang3)/4)#3 for angle is math opt
        if i == rangesetter-2:
           ang2 = ((ang1+ang3*side)/4)#3 for angle is math opt

        #special special case if both corners are touched punsish both ends, *3 is math opt but because distance is not accounted it sends p3 to infinity
        if i == rangesetter-2 and i == 1:
                ang2 = ((ang1*(side*0.66)+ang3*(side*0.66))/5) 

        #special case for worsening angle to prevent overcorrect (usually makes final result worse thus not used)
        if itera >1 and wtol != 0:
                
            if (abs(ang1-ang2/2))*wtol>abs(ang1):
                #ang2 = ang2- ((ang1-ang2/2)-ang1)
                ang2= 0
            if (abs(ang3-ang2/2))*wtol>abs(ang3):
                #ang2 = ang2- ((ang3-ang2/2)-ang3)
                ang2= 0
            #if ((ang1-ang2/2))*wtol>(ang1):
               #ang2 = ang2- ((ang1-ang2/2)-ang1)
            #   ang2= 0
            #if ((ang3-ang2/2))*wtol>(ang3):
               #ang2 = ang2- ((ang3-ang2/2)-ang3)
            #   ang2= 0
        return ang2
