#solve Trassenfinder
class Request:
    def __init__(self, polist):##unfinished
        self.polist = polist

  
def main():  
    #Create pointlist (polist) using user imput
    x1 = input("x 1:")
    x2 = input("x 2:")
    x3 = input("x 3:")
    x4 = input("x 4:")
    y1 = input("y 1:")
    y2 = input("y 2:")
    y3 = input("y 3:")
    y4 = input("y 4:")
    polist = [
        [x1,x2,x3,x4],
        [y1,y2,y3,y4]
    ]
    #polist range on first iteration is from [0][0] and [1][3]
    #create request as class (not sure why)
    request = Request(polist)

    for(){# amount of iterations (line versions)
        
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
        polist = polistnew
        #returns newpoints (all points spawned this iteration)

        for(){#amount of newpoint ( len(newpoints)
            from algorithm import pointmover
            if __name__ == '__main__':
                pointmover(#newpoint x and y)


