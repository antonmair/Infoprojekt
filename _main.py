from pointinserter import spawner
def curvecreator(polist):  
    #define amount of iterations
    iternumber = 12 
    #main loop
    for k in range(int(iternumber)):
        #insert and move points
        polist = spawner(polist, k)
    #print(polist)
    return polist

#curvecreator([(0.1,0.1),(0.2,0.2),(0.3,0.4),(0.5,0.6)])
