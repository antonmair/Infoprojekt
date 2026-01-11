import matplotlib.pyplot as plt
def polistplot(polist, plotvariant, i, iternumber, fig , ax):
    if plotvariant == 0:#initializer
        #define main pointlist
        polist = [[], []]

        #define plot settings
        ax.set_title("Click 4 Points")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.grid(True)
        plt.gca().set_aspect('equal')

        #register clicks
        def onclick(event):
            if event.inaxes != ax:
                return
            #insert points into polist
            polist[0].append(event.xdata)
            polist[1].append(event.ydata)

            #visual feedback for points
            ax.scatter(event.xdata, event.ydata, color='coral', s=50)
            #fig.canvas.draw_idle()

        cid = fig.canvas.mpl_connect('button_press_event', onclick)

        #lock until 4 points are inserted
        while len(polist[0])<4:
            plt.pause(0.05)
        #disable user input    
        fig.canvas.mpl_disconnect(cid)

        return polist
    elif plotvariant == 1:#iteration steps
        ax.set_title("Creating Curve...")
        alpha = (i+1)/iternumber
        ax.plot(polist[0], polist[1],  color='darkmagenta', linestyle='-', alpha = alpha, linewidth=2)
        #fig.canvas.draw_idle()
        plt.pause(1)
        return 0
    elif plotvariant == 2:#final curve
        #clear previos plots
        plt.cla()
        #redefine plot settings
        ax.set_title("Final Curve")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.grid(True)
        plt.gca().set_aspect('equal')

        ax.plot(polist[0], polist[1],  color='darkmagenta', linestyle='-', linewidth=2)
        #fig.canvas.draw_idle()
        plt.show()
        return 0
    # Keep window open at end







    # #set aspect ratio as equal
    # plt.gca().set_aspect('equal')
    # #more settings
    # fig, ax = plt.subplots()
    # ax.set_xlim(0, 10)
    # ax.set_ylim(0, 10)
    # ax.grid(True)
    # #plot
    # plt.plot(polist[0],polist[1])
    # #variable plot show time
    # #plt.pause(1)
