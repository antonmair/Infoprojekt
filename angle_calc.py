import math as math
def anglcalc(k, polist):
     anglist = []
     for i in range(2**(k)+1):
          angle = (math.atan2(polist[i+2][1] - polist[i+1][1], polist[i+2][0] - polist[i+1][0]) - math.atan2(polist[i][1] - polist[i+1][1], polist[i][0] - polist[i+1][0]))        
          if  angle < 0:
               angle =  angle * -1
               angle =  angle - math.pi
          elif angle >= 0:
               angle =  angle * -1
               angle =  angle + math.pi
          anglist.insert(i,(angle))  
     return anglist