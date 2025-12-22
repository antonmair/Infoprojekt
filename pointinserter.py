def spawner(polist):
    rangesetter = len(polist[0])-1
    i=0
    print(len(polist[0]))
    while i < rangesetter:
    #for i in range(rangesetter): bei vor kann man iterator nicht modifizieren weil python dumm ist
        #print(polist[0][i])
        if polist[0][i]!=polist[0][0] and polist[0][i]!=polist[0][-1] and polist[0][i]!=polist[0][-2]:
            polist[0].insert(i+1,((polist[0][i]+polist[0][i+1])/2))
            polist[1].insert(i+1,((polist[1][i]+polist[1][i+1])/2))
            i=i+1
            rangesetter = rangesetter + 1
            #polistnew = polist
        i=i+1
    print(polist)

    return polist
