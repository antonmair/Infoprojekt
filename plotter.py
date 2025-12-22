import matplotlib.pyplot as plt
def polistplot(polist):

    #vector 1
    endx1 = int(polist[0][1])
    startx1 =  int(polist[0][0])
    endy1 = int(polist[1][1])
    starty1 = int(polist[1][0]) 
    
    #vector 2
    endx2 = int(polist[0][-2])
    startx2 =  int(polist[0][-1])
    endy2 = int(polist[1][-2])
    starty2 = int(polist[1][-1])    

    #steigung v1
    deltax1 = endx1 - startx1
    deltay1 = endy1 - starty1

    #steigung v2
    deltax2 = endx2 - startx2
    deltay2 = endy2 - starty2

    plt.arrow(startx1, starty1, deltax1, deltay1, width=0.05)
    plt.arrow(startx2, starty2, deltax2, deltay2, width=0.05)

    plt.plot(polist[0],polist[1])
    plt.scatter(polist[0],polist[1])
    #dumb show
    #plt.show()

    #final dynamic show version
    plt.ioff()
    plt.gcf().show()

    #variable plot show time
    plt.pause(1)
    
