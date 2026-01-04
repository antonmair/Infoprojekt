from angle_calc import anglcalc
import math as math

def spawner(polist, itera):
    rangesetter = len(polist[0])-1 #rangsetter is amount of points and thus amount of iterations
    i=0
    afu = False
    nfu = False
    while i < rangesetter:
        if(i != 0 and i != rangesetter-1 and i != rangesetter): #check if point has to be created (dont create point if in start vectors)

            #define points to work with for current point
            p1x = float(polist[0][i-1])
            p1y = float(polist[1][i-1])
            #if(i>1): #funky alternative version that overcorrects + bug
            #    p1x = float(polist[0][i-2])
            #    p1y = float(polist[1][i-2])
            p2x = float(polist[0][i])
            p2y = float(polist[1][i])
            p3x = ((polist[0][i]+polist[0][i+1])/2) #this defines the new current points x
            p3y = ((polist[1][i]+polist[1][i+1])/2) #this defines the new current points y
            p4x = float(polist[0][i+1])
            p4y = float(polist[1][i+1]) 
            p5x = float(polist[0][i+2])
            p5y = float(polist[1][i+2]) 
            
            #define deltax and deltay of right triangle between p2, p3, finalp
            deltax = p3x - p2x
            deltay = p3y - p2y

            ang1, ang3, altformula = (anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y)) #calculates punishments with given points
            #print("original angles:", ang1,ang3, altformula)

            tempang1 = ang1
            #calculate optimal third angle based on deriative of general anglefunction (a - x / 2)² + x² + (b - x / 2)²
            ang2 = ((ang1+ang3)/3) #main function based on 2 as exponent
            #float(itera)
            #print(itera)
            #big stupid logic
            # if itera == 0:
            #     ang2 = ang2*2
            # if itera == 1:
            #     ang2 = ang2*1.5
            # elif itera == 2:
            #     ang2 = ang2*1
            # elif itera == 3:
            #     ang2 = ang2*0.8          
            # elif itera == 4:
            #     ang2 = ang2*0.8
            # elif itera == 5:
            #     ang2 = ang2*0.8
            # elif itera == 6:
            #     ang2 = ang2*0.8
            #more stupid logic
            #ang2 = ang2/((iterator+1)/2)
            
            #alt logic for big formula
            #if ang1<=ang3:
            #    ang2 = ang1
            #else:
            #    ang2 = ang3

            #ang2 = (ang1+ang3)/(2.75+0.05*iterator**2) #crazy variants divider works like exponent in other function
            #notes for dynamic verison
            #2+iterator*0.10 is not smooth but eliminates startend problem


            #would be version with higher expontential
            #n=2
            #n*x**(n-1)-(n*(g-x/2)**(n-1))/2-(n*(a-x/2)**n-1)/2 #difficult
            #x=(((n*(g-x/2)**(n-1))/2+(n*(a-x/2)**n-1)/2)/n)**(1/(n-1))

            #modify other two angles based on first on (check logic for pos neg)
            ang1=ang1-ang2/2
            ang3=ang3-ang2/2
            usedang1 = tempang1-ang1
            #usedang3 = tempang3-ang3

            #dev checks
            #print("angles: ",ang1, ang2, ang3)
            #print("delta: ", deltax, deltay)
            #print("p3: ", p3x,p3y)
            
            #formula for going left of line
            if altformula == False:
                finalx = (p2x+deltax-math.tan(usedang1*math.pi/180)*deltay)
                finaly = (p2y+deltay+math.tan(usedang1*math.pi/180)*deltax)
                nfu = True

            #formula for going right of line
            if altformula == True:
                finalx = (p2x+deltax+math.tan(usedang1*math.pi/180)*deltay)
                finaly = (p2y+deltay-math.tan(usedang1*math.pi/180)*deltax)
                afu = True
            #insert final point into polist
            polist[0].insert(i+1,(finalx))
            polist[1].insert(i+1,(finaly))

            #print(polist) #cosmetic

            #add an extra iteration and rangesetter because point has been added
            i=i+1
            rangesetter = rangesetter + 1
        i=i+1
    #if nfu == True and afu == True:
    #    itera = 0
    #    print("hi teher")



    return polist, itera
