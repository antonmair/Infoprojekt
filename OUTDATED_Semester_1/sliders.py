import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def slidercreate(fig, ax, iternumber, side, wtol):

    slider_ax  = fig.add_axes([0.93, 0.2, 0.03, 0.6])
    slider_ax1 = fig.add_axes([0.79, 0.2, 0.03, 0.6])
    slider_ax2 = fig.add_axes([0.65, 0.2, 0.03, 0.6])

    iterationsslider = Slider(
        ax=slider_ax,
        label="iterations",
        valmin=1,
        valmax=15,
        valinit=iternumber,
        valstep=1,
        orientation="vertical"
    )

    sideslider = Slider(
        ax=slider_ax1,
        label="side\nmultiplier",
        valmin=1,
        valmax=5,
        valinit=side,
        orientation="vertical"
    )

    worseningslider = Slider(
        ax=slider_ax2,
        label="worsening\nprohibitor",
        valmin=0,
        valmax=1,
        valinit=wtol,
        orientation="vertical"
    )

    def update_iterations(val):
        nonlocal iternumber
        iternumber = int(val)

    def update_side(val):
        nonlocal side
        side = int(val)

    def update_wtol(val):
        nonlocal wtol
        wtol = val

    iterationsslider.on_changed(update_iterations)
    sideslider.on_changed(update_side)
    worseningslider.on_changed(update_wtol)

    #keep sliders enabled
    fig._sliders = iterationsslider, sideslider, worseningslider

    plt.show(block=False)

    #return iternumber, side, wtol
    return iterationsslider, sideslider, worseningslider
