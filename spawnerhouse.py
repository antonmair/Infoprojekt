import math as math
import geopandas as gpd
from scipy.optimize import root_scalar
from shapely.geometry import Point
from angle_calc import anglcalc
from scipy.optimize import minimize_scalar

def spawnerh(polist, k, building_gdf,angle_weight,first_value,second_value):#k is iteration were on
    #call anglcalc for anglist
    anglist = anglcalc(k, polist)

    #range and iteration logic based on old first semester project
    rangesetter = len(polist) - 2
    i = 1
    angleitera = 0
    while i < rangesetter:
        #seperate current point coordinates
        p2x, p2y = polist[i]
        
        #seperate new midpoint coordinates
        p3x = (polist[i][0] + polist[i + 1][0]) / 2
        p3y = (polist[i][1] + polist[i + 1][1]) / 2

        #calculate difference
        deltax = p3x - p2x
        deltay = p3y - p2y
        
        #lenght is radius around midpoint
        length = (deltax**2 + deltay**2)**0.5

        #housebounds = math.sqrt(length*1000) #retest this might work better
        housebounds = length

        #calculate normale steigung
        dxf = -deltay / length
        dyf = deltax / length

        #combine p3 as point
        basepoint = Point(p3x, p3y)

        #generates house search area
        if k<8:#limits to first iteration because houses no longer relevant for last few meters
            nearby_buildings = building_gdf[
                building_gdf.geometry.distance(basepoint) <= housebounds
            ]
            house_coords = [
                (point.x, point.y)
                for point in nearby_buildings.geometry
            ]
        else: 
            house_coords=[]
        house_count = len(house_coords)

        #curve calculation
        def houses_derivative(x):
            a = anglist[angleitera]
            c = anglist[angleitera+1]
        
            x1, y1 = polist[i]
            x2, y2 = polist[i + 1]
            
            L = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)#could still implement extra weighted part for first and last angles but marginal with house part
        
            s = 2 * math.atan(2 * x / L)
        
            angle= (a - 0.5 * s)**2 + s**2 + (c - 0.5 * s)**2 
            
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
                total += first_value / d + d / (2001-second_value)

            #if houses are here    
            if house_count!=0:
                anglepart += (angle)*angle_weight*k**2
                total+=anglepart
            #if no houses are here
            else:
                total = angle

            return total

        #use minimum function
        result = minimize_scalar(#using minimum instead of root because to lazy to do manual real derivateive of 200/h and h/200 and maybe doesnt work because of brenq method and diffrents signs on bound ends, but might be faster if derivative hardcoded
            houses_derivative,
            bounds=(housebounds*-0.9,housebounds*0.9),#0.9 so it stays within housebounds
            method="bounded"
        )

        x_zero = result.x

        #calculate final points
        finalx = p3x + x_zero * dxf
        finaly = p3y + x_zero * dyf

        #insert into polist
        polist.insert(i + 1, (finalx, finaly))

        #more range logic
        i = i + 2
        rangesetter = rangesetter + 1
        angleitera = angleitera + 1

    return polist
