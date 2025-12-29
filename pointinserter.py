import math as math
from angle_calc import anglcalc
from angle_punishment import anglescript

def spawner(polist):
    rangesetter = len(polist[0])-1
    i=0
    #print(len(polist[0]))
    while i < rangesetter:
        #print("checking...")
        if(i != 0 and i != rangesetter-1 and i != rangesetter):#this should work
        #if polist[0][i]!=polist[0][0] and polist[0][i]!=polist[0][-1] and polist[0][i]!=polist[0][-2]:#this logic is flawed because it doesnt check for position within list but for values witch chan be the same fore diffrent positions
            #print("how often do you do this?")
            #print("this message should appear",rangesetter-2,"times")
            #----algorithm for pointmover----

            p1x = int(polist[0][i-1])
            p1y = int(polist[1][i-1])
            p2x = int(polist[0][i])
            p2y = int(polist[1][i])
            p3x = ((polist[0][i]+polist[0][i+1])/2)
            p3y = ((polist[1][i]+polist[1][i+1])/2)
            p4x = int(polist[0][i+1])
            p4y = int(polist[1][i+1]) 
            p5x = int(polist[0][i+2])
            p5y = int(polist[1][i+2]) 
            
            deltax = p4x - p2x
            deltay = p4y - p2y

            #general setup for pointmover
            finalx = p3x
            finaly = p3y
            spacing = 0.05 #sets search spacing
            punishment = anglescript(anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y))

            #first loop inverting deltax (search left of line)
            j=0
            tempdx=deltax
            deltax=deltay*-1
            deltay=tempdx
            while j <= (0.50-spacing):#constrain search radius within half of dist p+1 p-1
                #print("variation", p3x,p3y)
                p3x = p3x+spacing*deltax
                p3y = p3y+spacing*deltay
                j=j+spacing
                newcalcpun = anglescript(anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y))
                if  newcalcpun <= punishment: #using <= only in test version remove later
                    #print("do you ever get here1", deltax, deltay)
                    finalx = p3x
                    finaly = p3y
                    punishment = newcalcpun

            #second loop inverting deltay (search right of line)
            p3x = ((polist[0][i]+polist[0][i+1])/2) #resets p3x
            p3y = ((polist[1][i]+polist[1][i+1])/2) #resets p3y
            j=0
            deltax = deltax*-1
            deltay = deltay*-1
            #print("lengt of 1", math.sqrt(deltax*deltax+deltay*deltay))
            while j <= (0.50-spacing):
                p3x = p3x+spacing*deltax
                p3y = p3y+spacing*deltay
                j=j+spacing
                newcalcpun = anglescript(anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y))
                if  newcalcpun <= punishment: #using <= only in test version remove later
                    #print("do you ever get here2", deltax, deltay)
                    finalx = p3x
                    finaly = p3y
                    punishment = newcalcpun

            #insert final point into polist
            print("THISSS", finalx, finaly)
            polist[0].insert(i+1,(finalx))
            polist[1].insert(i+1,(finaly))

            i=i+1
            rangesetter = rangesetter + 1 #do we still need rangesetter???
        i=i+1
    return polist
