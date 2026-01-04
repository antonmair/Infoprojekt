from angle_calc import anglcalc
def spawner(polist, itera):
    rangesetter = len(polist[0])-1 #rangsetter is amount of points and thus amount of iterations
    i=0
    isfirst = False
    islast = False
    while i < rangesetter:
        if(i != 0 and i != rangesetter-1 and i != rangesetter): #check if point has to be created (dont create point if in start vectors)
            if i == 1:
                isfirst = True
            if i == rangesetter-2:
                islast = True
            #define points to work with for current point
            p1x = float(polist[0][i-1])
            p1y = float(polist[1][i-1])
            #if i> 1: #funky alternative version that overcorrects
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
            
            #define deltax and deltay
            deltax = p4x - p2x
            deltay = p4y - p2y

            #general setup for pointmover
            spacing = 0.0001 #sets search spacing
            finalx = p3x
            finaly = p3y
            punishment = anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y, itera, isfirst, islast) #calculates punishments with given points
            #print("importatn", punishment)
            #first loop inverting deltax (search left of line)
            j=0.0 #iterator

            #changing deltax/y for first direction (normal of deltax/y)
            tempdx=deltax
            deltax=deltay*-1
            deltay=tempdx

            while j <= (0.50-spacing):#0.50 constrains search radius within half of dist deltax/y
                #print("variation", p3x,p3y)
                p3x = p3x+spacing*deltax
                p3y = p3y+spacing*deltay
                j=j+spacing
                #newcalcpun = anglescript(anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y)) #calculates punishments with given points
                newcalcpun = anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y, itera, isfirst, islast)
                #print("newcalcpun iteration a", newcalcpun)
                if  newcalcpun <= punishment: #if better solution found insert as preliminary finalist #using <= only in test version remove later
                    finalx = p3x
                    finaly = p3y
                    punishment = newcalcpun

            #second loop inverting deltay (search right of line)
            j=0.0 #iterator
    
            #changing deltax/y for second direction (normal of deltax/y)
            deltax = deltax*-1
            deltay = deltay*-1
            
            #reset p3x and p3y
            p3x = ((polist[0][i]+polist[0][i+1])/2)
            p3y = ((polist[1][i]+polist[1][i+1])/2) 

            while j <= (0.50-spacing):#0.50 constrains search radius within half of dist deltax/y
                p3x = p3x+spacing*deltax
                p3y = p3y+spacing*deltay
                j=j+spacing
                #newcalcpun = anglescript(anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y))
                newcalcpun = anglcalc(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y, itera, isfirst, islast)
                #print("newcalcpun iteration a", newcalcpun)
                if  newcalcpun <= punishment: #if better solution found insert as preliminary finalist #using <= only in test version remove later
                    finalx = p3x
                    finaly = p3y
                    punishment = newcalcpun

            #insert final point into polist
            polist[0].insert(i+1,(finalx))
            polist[1].insert(i+1,(finaly))

            #add an extra iteration and rangesetter because point has been added
            i=i+1
            rangesetter = rangesetter + 1
        i=i+1

    return polist
