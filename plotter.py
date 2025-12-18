import matplotlib.pyplot as plt
def polistplot(polist):
    #print(polist[0][1])
    endx = int(polist[0][1])
    startx =  int(polist[0][0])
    endy = int(polist[1][1])
    starty = int(polist[1][0])

    # deltax = polist[0][1] - polist[0][0]
    # deltay = polist[1][1] - polist[1][0]
    deltax = endx - startx
    deltay = endy - starty
    print(startx)
    print(starty)
    plt.arrow(1, 5, 1, 2, width=0.05)
    plt.arrow(startx, starty, deltax, deltay, width=0.05)
    # del polist[0][0]
    # del polist[1][0]
    # del polist[0][len(polist)]
    # del polist[1][len(polist)]
    plt.plot(polist[0],polist[1])
    plt.show()
