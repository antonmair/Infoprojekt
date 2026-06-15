import math as math
def polistcalc(polist, anglist, newanglist):
    rangesetter = len(polist)-2
    i=1
    angleitera = 0
    while i < rangesetter:
        p2x, p2y = polist[i]
        p3x = (polist[i][0] + polist[i + 1][0]) / 2
        p3y = (polist[i][1] + polist[i + 1][1]) / 2
        ang1 = anglist[angleitera]
        ang2 = newanglist[angleitera]
        usedang1 = ang1-(ang1-ang2/2)
        deltax = p3x - p2x
        deltay = p3y - p2y
        finalx = (p2x+deltax-math.tan(usedang1)*deltay)
        finaly = (p2y+deltay+math.tan(usedang1)*deltax)
        polist.insert(i + 1, (finalx, finaly))
        i=i+2
        rangesetter = rangesetter + 1
        angleitera = angleitera + 1
    return polist