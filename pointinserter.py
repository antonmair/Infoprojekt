def spawner(polist):
    for i in range(len(polist)):
            #why just one iteration??????
        #if polist[0][i]!=polist[0][0] & polist[0][i]!=polist[len(polist[0])] & polist[0][i]!=polist[len(polist[0]-1)]:
            polist.insert(i,((polist[0][i]+polist[0][i+1])/2, (polist[1][i]+polist[1][i+1])/2))
            #polistnew = polist
            print(polist)
            return polist
