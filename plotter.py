import matplotlib.pyplot as plt
def polistplot(polist):
    plt.plot(polist[0],polist[1])
    #plt.scatter(polist[0],polist[1])
    plt.ioff()
    plt.gcf().show()
    plt.gca().set_aspect('equal')

    #variable plot show time
    plt.pause(1)
