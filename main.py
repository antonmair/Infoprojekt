#solve Trassenfinder
class Request:
    def __init__(self, polist):##unfinished
        self.polist = polist

  
def main():  
    #Create pointlist (polist) using user imput
    x1 = input("x 1:")#start of vec1 x
    x2 = input("x 2:")#end of vec1 x 
    x3 = input("x 3:")#end of vec2 x
    x4 = input("x 4:")#start of vec2 x
    y1 = input("y 1:")#start of vec1 y
    y2 = input("y 2:")#end of vec 1 y 
    y3 = input("y 3:")#end of vec 2 y
    y4 = input("y 4:")#start of vec 2 y
    polist = [
        [x1,x2,x3,x4],
        [y1,y2,y3,y4]
    ]
    #polist range on first iteration is from [0][0] and [1][3]
    #first index 0 = x 1 = y
    #create request as class (not sure why)
    request = Request(polist)

    for i in range(5):# amount of iterations (line versions)
        
        #plot polist
        from plotter import polistplot
        if __name__ == '__main__':
            polistplost(polist)
        
        #calculate angles
        from angle_calc import anglcalc
        if __name__ == '__main__':
            anglcalc(polist)#to check: does anglcalc need polist and why and when (is correct usage of anglcalc(polist)) same for the others
        #returns anglearr
        
        #calculate punishment
        from angle_punishment import anglescript
        if __name__ == '__main__':
            anglescript(anglearr)
        #returns penalty
        
        #insert points
        from pointinserter import spawner
        if __name__ == '__main__':
            spawner(polist)#spawns points between every x and y point in array at half way but not betwen first and second, and penult and ult
        #returns polistnew 
        #returns newpoints (all points spawned this iteration)

        for j in range(len(newpoints)):#amount of newpoint ( len(newpoints)
            
            #moves one point
            from algorithm import pointmover
            if __name__ == '__main__':
                pointmover(polistnew[0][i],polistnew[1][i]) #function pointmover calls anglcalc and aglescript seperatly within the algorithm.py file
                #returns newx, newy (x and y of best newpoint)
                polistnew[0][i] = newx
                polistnew[1][i] = newy
        }

        #end of iteration finalize changes into polist
        polist = polistnew
    }


