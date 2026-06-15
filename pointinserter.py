from angle_calc import anglcalc
from angle_punishment import anglepunishment
from polistupdate import polistcalc
def spawner(polist, k):
    anglist = anglcalc(k, polist)#calculates existing angles
    newanglist = anglepunishment(k, anglist)#calculates new angles based on existing angles and curve smoothing matrix
    polist = polistcalc(polist, anglist, newanglist) #inserts new points based on new angles into polist
    return polist