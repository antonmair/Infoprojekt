import matplotlib.pyplot as plt
import numpy as np

def polistplot(polist, plotvariant, i, iternumber, fig , ax, side, wtol):
    if plotvariant == 0:#initializer

        #define main pointlist
        polist = [[], []]
        plt.subplots_adjust(right=0.6)

        #define plot settings
        ax.set_title("Click 4 Points")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.grid(True)
        plt.gca().set_aspect('equal')

        #create sliders
        from sliders import slidercreate
        iterationsslider, sideslider, worseningslider = slidercreate(fig, ax, iternumber, side, wtol)  

        #register sloder changes
        slider_values = {'iternumber': iternumber, 'side': side, 'wtol': wtol}
        
        #check for slider input
        def update_iterations(val):
            slider_values['iternumber'] = int(val)
        def update_side(val):
            slider_values['side'] = int(val)
        def update_wtol(val):
            slider_values['wtol'] = val

        #connect the changes to the sliders
        iterationsslider.on_changed(update_iterations)
        sideslider.on_changed(update_side)
        worseningslider.on_changed(update_wtol)

        #check for point input
        def onclick(event):
            #ignore clicks outside axes or without data coordinates
            if event.inaxes != ax or event.xdata is None or event.ydata is None:
                return iternumber, side, wtol
            
            #insert points into polist
            polist[0].append(event.xdata)
            polist[1].append(event.ydata)

            #visual feedback for points
            ax.scatter(event.xdata, event.ydata, color='coral', s=30)

        #configure disconnect
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        
        #lock until 4 points are inserted
        while len(polist[0])<4:
            plt.pause(0.05)

            #constantly read new slider inputs
            iternumber = slider_values['iternumber']
            side = slider_values['side']
            wtol = slider_values['wtol']

        #disable user input    
        fig.canvas.mpl_disconnect(cid)

        return polist, iternumber, side, wtol
    
    #-------------------------------------
    elif plotvariant == 1:#iteration steps

        #new title
        ax.set_title("Creating Curve...")

        #relim
        xmin = min(polist[0])
        if xmin > 0:
            xmin = 0
        xmax = max(polist[0])
        if xmax < 100:
            xmax = 100
        ymin = min(polist[1])
        if ymin > 0:
            ymin = 0
        ymax = max(polist[1])
        if ymax < 100:
            ymax = 100

        #set new limits
        ax.set_xlim(xmin+np.sign(xmin)*10, xmax+np.sign(xmax)*10)
        ax.set_ylim(ymin+np.sign(ymin)*10, ymax+np.sign(ymax)*10)

        #change opacity based on iteration
        alpha = (i+1)/iternumber
        ax.plot(polist[0], polist[1],  color='darkmagenta', linestyle='-', alpha = alpha, linewidth=1.5)
        
        #pause plot
        plt.pause(1)

        return 0
    
    #-------------------------------------
    elif plotvariant == 2:#final curve

        #clear previos plots
        ax.cla()

        #redefine plot settings
        ax.set_title("Final Curve")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.grid(True)
        plt.gca().set_aspect('equal')

        #relim
        xmin = min(polist[0])
        if xmin > 0:
            xmin = 0
        xmax = max(polist[0])
        if xmax < 100:
            xmax = 100
        ymin = min(polist[1])
        if ymin > 0:
            ymin = 0
        ymax = max(polist[1])
        if ymax < 100:
            ymax = 100

        #set new limits
        ax.set_xlim(xmin+np.sign(xmin)*10, xmax+np.sign(xmax)*10)
        ax.set_ylim(ymin+np.sign(ymin)*10, ymax+np.sign(ymax)*10)
        
        #plot
        ax.plot(polist[0], polist[1],  color='darkmagenta', linestyle='-', linewidth=1.5)
        
        #pause plot
        plt.show()

        return 0
