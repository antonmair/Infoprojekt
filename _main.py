import matplotlib.pyplot as plt
def main():  
    #default settings
    iternumber = 12 
    side = 3.0
    wtol = 0.0
    #define plots
    fig, ax = plt.subplots()

    #plot input field
    plotvariant = 0
    from plotter import polistplot
    if __name__ == '__main__':
        polist, iternumber, side, wtol  = polistplot(0, plotvariant, 0, iternumber, fig, ax, side, wtol)    


    #go to iteration step plot variant
    plotvariant = 1

    #main loop
    for i in range(int(iternumber)):

        #insert and move points
        from pointinserter import spawner
        if __name__ == '__main__':
            polist = spawner(polist, i, side, wtol)

        #show iteration steps
        if i < 6:
            from plotter import polistplot
            if __name__ == '__main__':
                polistplot(polist, plotvariant, i, iternumber, fig, ax, 0, 0)  

    #final display after curve is finished
    plotvariant = 2
    from plotter import polistplot
    if __name__ == '__main__':
        polistplot(polist, plotvariant, 0, 0, fig, ax, 0, 0) 

main()
