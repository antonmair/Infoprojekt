import matplotlib.pyplot as plt

class Request:
    def __init__(self, polist):
        self.polist = polist


def main(x1,x2,x3,x4,y1,y2,y3,y4):  
    #Create pointlist (polist) using user imput
    # x1 = input("x 1:")#start of vec1 x
    # x2 = input("x 2:")#end of vec1 x 
    # x3 = input("x 3:")#end of vec2 x
    # x4 = input("x 4:")#start of vec2 x
    # y1 = input("y 1:")#start of vec1 y
    # y2 = input("y 2:")#end of vec 1 y 
    # y3 = input("y 3:")#end of vec 2 y
    # y4 = input("y 4:")#start of vec 2 y
    
    #dev version

    #somethin
    # x1=1
    # x2=1
    # x3=3
    # x4=2
    # y1=1
    # y2=2
    # y3=4
    # y4=5
    
    
    
    


    # x1=2
    # x2=2
    # x3=5
    # x4=6
    # y1=1
    # y2=2
    # y3=5
    # y4=5

    # x1=1
    # x2=2
    # x3=20
    # x4=21
    # y1=5
    # y2=6
    # y3=21
    # y4=22

    # x1=1
    # x2=2
    # x3=3
    # x4=4
    # y1=5
    # y2=6
    # y3=7
    # y4=8

    # x1=1
    # x2=2
    # x3=8
    # x4=9
    # y1=3
    # y2=3
    # y3=3
    # y4=3
    
    polist = [
        [x1,x2,x3,x4],
        [y1,y2,y3,y4]
    ]
    #polist range on first iteration is from [0][0] and [1][3]
    #first index 0 = x 1 = y
    #create request as class (not sure why)
    request = Request(polist)
    itera = 0
    print("------------------------")
    for i in range(12):# amount of iterations (line versions) sollte nicht ueber 10 sein weil to much
        itera = itera + 1

        #insert and move points
        from pointinserter import spawner
        if __name__ == '__main__':
            polist, itera = spawner(polist,itera)

        #plot polist
        from plotter import polistplot
        if __name__ == '__main__':
            polistplot(polist)


main(2,1,3,2,1,1,1,1)
plt.pause(20000)#pause plot on final iteration
    #inverted
    # x1=2
    # x2=1
    # x3=4
    # x4=5
    # y1=1
    # y2=1
    # y3=1
    # y4=1
main(2,1,4,5,1,1,1,1)
plt.pause(20000)#pause plot on final iteration
    #upper left
    # x1=1
    # x2=1
    # x3=3
    # x4=4
    # y1=1
    # y2=2
    # y3=4
    # y4=4
main(1,1,3,4,1,2,4,4)
plt.pause(20000)#pause plot on final iteration
    #upper right
    # x1=4
    # x2=5
    # x3=6
    # x4=6
    # y1=4
    # y2=4
    # y3=3
    # y4=2
main(4,5,6,6,4,4,3,2)
plt.pause(20000)#pause plot on final iteration
    #lower right
    # x1=1
    # x2=2
    # x3=4
    # x4=4
    # y1=1
    # y2=1
    # y3=3
    # y4=4
main(1,2,4,4,1,1,3,4)
plt.pause(20000)#pause plot on final iteration
    # #lower right
    # x1=1
    # x2=1
    # x3=2
    # x4=3
    # y1=3
    # y2=2
    # y3=1
    # y4=1
main(1,1,2,3,3,2,1,1)
plt.pause(20000)#pause plot on final iteration
    #inverted
    # x1=2
    # x2=1
    # x3=4
    # x4=5
    # y1=1
    # y2=1
    # y3=1
    # y4=1
main(0,1,4,5,1,1,4,4)
plt.pause(20000)#pause plot on final iteration


from angle_calc import anglcalc
# print(anglcalc(0,0,-1,1,99,99,1,1,0,0))

#print(anglcalc(0,0,-1,-1,99,99,1,-1,0,0))


