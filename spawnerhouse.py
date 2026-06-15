#for some reason it keeps summing polists 
import math as math
import geopandas as gpd
#p3x/y is in degrees
#basepoint_proj is in meteres
#everything should be in meters
def spawnerh(polist, k, building_gdf):
    print("SPAWNERH CALLED")
    rangesetter = len(polist)-2
    i=1
    angleitera = 0
    while i < rangesetter:
        #p2x, p2y = polist[i]
        p2y,p2x = polist[i]#inverted for some reason
        #p3x = (polist[i][0] + polist[i + 1][0]) / 2#midpoint x base
        #p3y = (polist[i][1] + polist[i + 1][1]) / 2#midpoint y base
        #p3y = (polist[i][0] + polist[i + 1][0]) / 2#midpoint x base#inverted for some reason
        #p3x = (polist[i][1] + polist[i + 1][1]) / 2#midpoint y base
        p3x = (polist[i][0] + polist[i + 1][0]) / 2 #uninverted variant
        p3y = (polist[i][1] + polist[i + 1][1]) / 2
        deltax = p3x - p2x
        deltay = p3y - p2y
        dxf = deltax/(deltax**2+deltay**2)**0.5#values are between 1 and 0 where 1 is completly in completlypointing east/north respectivly and 0 isno chng in x/y
        dyf = deltay/(deltax**2+deltay**2)**0.5
        
        dyx= dyf#change rotation to account for being on helpline not on miainline
        dxf=-dxf
        
        #dxf = deltax
        #dyf = deltay
        print("dxf,dyf",dxf,dyf)
        #combinedhousefunction
        #cbhf= dyf(dyf
        #combine house function with angle function (later
        #cbf= cbhf+af*len(building_gdf)
                  
        #nullsetz house function
        from scipy.optimize import newton 
        from scipy.optimize import root_scalar
        from shapely.geometry import Point
        #basepoint= p3x, p3y
        basepoint = Point(p3x, p3y)
        #collect houses within 500m
        #nearby_buildings = building_gdf[
        #    building_gdf.geometry.distance(basepoint) <= 500/111320.0# UserWarning: Geometry is in a geographic CRS. Results from 'distance' are likely incorrect. Use 'GeoSeries.to_crs()' to re-project geometries to a projected CRS before this operation.
        #]

        
        #basepoint_gdf = gpd.GeoSeries([basepoint], crs=building_gdf.crs)

        #building_proj = building_gdf.to_crs(3857)#this is inaccurate and in degrees i think
        #basepoint_proj = basepoint_gdf.to_crs(3857).iloc[0]
        
        #utm_crs = building_gdf.estimate_utm_crs()#this is better
        #building_gdf = building_gdf.to_crs(utm_crs)
        
        nearby_buildings = building_proj[
            building_proj.geometry.distance(basepoint_proj) <= 500
        ]
        print("basepoint koordiantes",basepoint_proj)
        #print("basepoint x", basepoint_proj.x,"dxf", dxf)
        #print("basepoint y", basepoint_proj.y,"dyf", dyf)
        house_coords = [
            (point.x, point.y)
            for point in nearby_buildings.geometry
        ]
        print("house coordiantes",house_coords)
        #big house function function
        def houses_derivative(x):
            total = 0.0

            for dxn, dyn in house_coords:#this is called howerver oftern brentq thinks is sensible
                #why  twice for one hoese?
                #print("basepoint x", basepoint_proj.x,"dxn", dxn, "substraction", basepoint_proj.x-dxn)
                #print("basepoint y", basepoint_proj.y,"dyn", dyn, "substraction",basepoint_proj.y-dyn)
                denominator = (
                    (dyf * x - (dyn-basepoint_proj.y)) ** 2
                    +(dxf * x - (dxn-basepoint_proj.x)) ** 2#vielleicht statt p3x/y basepointf usdiofjaber wichtig (main problem)
                ) ** 0.5

                if denominator > 1e-12:
                    total += (
                        dyf * (dyf * x - (dyn-basepoint_proj.y))#completly review logic of even using the derivative
                        + dxf * (dxf * x - (dxn-basepoint_proj.x))#vielleicht statt p3x/y basepointf usdiofjaber wichtig (main problem)
                    ) / denominator
                else:
                    print("bad")
            #total = 1/(total+1)#awaymover
            return total

        #debug print
        #fa = houses_derivative(-1000)
        #fb = houses_derivative(1000)
        #print("fa =", fa)
        #print("fb =", fb)
        
        result = root_scalar(
            houses_derivative,
            bracket=[-100000, 100000],  #adjust if necessary #what units are 1000?????
            method="brentq"
        )
        #x_zero = newton(houses_derivative, x0=0.0)
        x_zero=result.root
        #fa = houses_derivative(-1000)
        #fb = houses_derivative(1000)

        #if fa * fb > 0:
        #    x_zero = 0.0
        #else:
        #    result = root_scalar(
        #        houses_derivative,
        #        bracket=[-1000,1000],
        #        method="brentq"
        #    )
        #x_zero = result.root

        print("Derivative zero at:", x_zero)
        print("Derivative zero at(brentq:", result)

        #finalx = p3x+x_zero/dxf #review math logic
        #finaly = p3y+x_zero/dyf #review math logic

        nx = dyf*2##-is above
        ny = dxf*2
        #nx= -dyf#original
        #ny=dxf
        
        #conversion from meters to degrees cause idiotic
        lat = p3y  #if using (lon, lat)

        #meters_per_deg_lat = 111320 #umrechnungs wird jetzt schon vorher nicht in diesem code gemacht
        #meters_per_deg_lon = 111320 * math.cos(math.radians(lat))

        delta_lon = (x_zero * nx)# / meters_per_deg_lon#is dividing really correct?
        delta_lat = (x_zero * ny)# / meters_per_deg_lat#this is still the problem
        print("Verschiebugng",delta_lat,delta_lon)
        finalx = p3x + delta_lon#in degrees for both# for some reason it ignores pos neg
        finaly = p3y + delta_lat

        #finalx = p3x + x_zero * nx
        #finaly = p3y + x_zero * ny

        #dxxf and dyf have to be rotated 90° because of the helper line beeing normal on ml


        
        #finalx = #(p2x+deltax-math.tan(usedang1)*deltay)
        #finaly = #(p2y+deltay+math.tan(usedang1)*deltax)
        #polist.insert(i + 1, (finaly, finalx)) #inverted
        polist.insert(i + 1, (finaly, finalx)) #uninverted because in meters from beginning

        i=i+2
        rangesetter = rangesetter + 1
        angleitera = angleitera + 1

    return polist