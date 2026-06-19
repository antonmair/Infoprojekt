#latitude is russia-usa and x ai sais this is wrong fo r som e reason 
#longitude is south africa-poland and y
import math as math
import geopandas as gpd
from scipy.optimize import root_scalar
from shapely.geometry import Point
from angle_calc import anglcalc
from scipy.optimize import minimize_scalar

def spawnerh(polist, k, building_gdf,angle_weight,first_value,second_value):#k is iteration were on
    #print("SPAWNERH CALLED with len(polist)=", len(polist))7
    
    anglist = anglcalc(k, polist)
    
    rangesetter = len(polist) - 2
    i = 1
    angleitera = 0

    while i < rangesetter:
        p2x, p2y = polist[i]

        p3x = (polist[i][0] + polist[i + 1][0]) / 2
        p3y = (polist[i][1] + polist[i + 1][1]) / 2

        deltax = p3x - p2x
        deltay = p3y - p2y
        
        #print("deltax/y", deltax, deltay)
        #lenght is radius around midpoint
        length = (deltax**2 + deltay**2)**0.5
        #housebounds = math.sqrt(length*1000) #retest this might work better
        housebounds = length

        dxf = -deltay / length
        dyf = deltax / length
        
        #print("dxf,dyf", dxf, dyf)

        basepoint = Point(p3x, p3y)

        nearby_buildings = building_gdf[#maybe visibly display bounds with polygon
            building_gdf.geometry.distance(basepoint) <= housebounds#dynamic radius based on iteration is very very essential to implemnt #500 current base#2k is good
        ]
        #print("radius", housebounds)
        #print("basepoint koordiantes", basepoint)
        if k<7:
            house_coords = [
                (point.x, point.y)
                for point in nearby_buildings.geometry
            ]
        else: 
            house_coords=[]
        house_count = len(house_coords)
        #print("house coordiantes", house_coords)
        #if not house_coords: #might crash if this is commented hope not
        #    print("no nearby buildings")
        #    i = i + 1
        #    continue
            

        #def f_angle_shift(x, k, polist, i):#
        #def f_angle_shift(x):
        #    anglist = anglcalc(k, polist)
       # 
       #     a = anglist[i - 1]
       #     c = anglist[i]
       # 
        #    x1, y1 = polist[i]
        #    x2, y2 = polist[i + 1]
        #
        #    L = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        #
        #    x = 2 * math.atan(2 * s / L)
        #
       #     return (a - 0.5 * x)**2 + x**2 + (c - 0.5 * x)**2

        
        def houses_derivative(x):
            #angle part
            #anglist = anglcalc(k, polist) #why did i put this here in the first place?? is at start now
            #print(
            #    "angleitera =", angleitera,
            #    "len(anglist) =", len(anglist)
            #)
            a = anglist[angleitera]#why is this still out of bounds for higher iterations?
            c = anglist[angleitera+1]#why is this still out of bounds for higher iterations?
        
            x1, y1 = polist[i]
            x2, y2 = polist[i + 1]
        
            L = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)#still have to implement extra weighted part for first and last angles
        
            s = 2 * math.atan(2 * x / L)
        
            angle= (a - 0.5 * s)**2 + s**2 + (c - 0.5 * s)**2 
            #print(angle)
            
            #house part
            total = 0.0
            anglepart = 0.0
            
            for dxn, dyn in house_coords:#final was 25000 200 and 2000000
                dxd = dxn - basepoint.x
                dyd = dyn - basepoint.y
                d = (
                    (dxd - dxf * x) ** 2
                    + (dyd - dyf * x) ** 2
                ) ** 0.5
                total += first_value / d + d / second_value#base is 200 200 now i try 1000 500 # first value is more punishment for closer value second value is more punishment for to far away 50.000 an 100? 500 second value is way to much #100 sv might be too direct #sv as a slider is the s slider 2X SLIDER #to scared of houses
                #print("thisnot", k)
                #total=total/house_count#logic here is to always weight the same here regardless of amount of houses correction happens in the angle part #imf fuc this shit doesnt even work well
            print("house pun", total)#change general punishment based on total amount of houses and distance
            if house_count!=0:
                anglepart += (angle*house_count/house_count)*angle_weight*k**2#this has to be dynamic as well#100 is entirely approximate might be a slider mynbe 200 SLIDER #why the fuck was it *house_count #had ten with *house_count times house count is done because more houses means more value in the top part which needs more value in the bottom part so it doues maek esense
                total+=anglepart
                print("angle pun", anglepart)
            else:
                total = angle
            #else:
            #    print("bad")

            return total
        
        #result = root_scalar(
        result = minimize_scalar(#using minimum instead of root because to lazy to do manual real derivateive of 200/h and h/200 but might be faster if derivative hardcoded
            houses_derivative,
            #bracket=[-10000, 10000],#THIS COULD BE DYNAMIc based off of p3 to p2 distance#this dynamic constrains the minimum to stay within houses-bound which is set by the iteration dynamic (currently linear 500m) as describet by a comment above
            #bounds=(-1000,1000),#these bounds are way better if using only the house algorithm but thats not the point
            bounds=(housebounds*-0.9,housebounds*0.9),#0.9 so it stays within housebounds
            method="bounded"
            #method="brentq"#comment in the line above is improtant
        )

        #x_zero = result.root
        x_zero = result.x

        #print("Derivative zero at:", x_zero)
        #print("Derivative zero at(brentq:", result)
        #print("Minimum at:", x_zero)
        #print("Minimize result:", result)
        #print("Verschiebugng", delta_lat, delta_lon)

        finalx = p3x + x_zero * dxf
        finaly = p3y + x_zero * dyf

        polist.insert(i + 1, (finalx, finaly))

        i = i + 2
        rangesetter = rangesetter + 1
        angleitera = angleitera + 1

    return polist
