import matplotlib.pyplot as plt
def main():  

    #define amount of iterations    
    iternumber = 8

    #define plots
    fig, ax = plt.subplots()

    #plot input field
    plotvariant = 0
    from plotter import polistplot
    if __name__ == '__main__':
        polist = polistplot(0, plotvariant, 0, 0, fig, ax)    

    #go to iteration step plot variant
    plotvariant = 1

    #main loop
    for i in range(int(iternumber)):

        #insert and move points
        from pointinserter import spawner
        if __name__ == '__main__':
            polist = spawner(polist)

        #show iteration steps
        from plotter import polistplot
        if __name__ == '__main__':
            polistplot(polist, plotvariant, i, iternumber, fig, ax)  

    #final display after curve is finished
    plotvariant = 2
    from plotter import polistplot
    if __name__ == '__main__':
        polistplot(polist, plotvariant, 0, 0, fig, ax) 

main()
