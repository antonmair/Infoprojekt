#latitude is russia-usa and x ai sais this is wrong fo r som e reason 
#longitude is south africa-poland and y



import math as math
import geopandas as gpd

#everything should be in meters
def spawnerh(polist, k, building_gdf):
    print("SPAWNERH CALLED")
    rangesetter = len(polist) - 2
    i = 1
    angleitera = 0

    while i < rangesetter:
        p2x, p2y = polist[i]

        p3x = (polist[i][0] + polist[i + 1][0]) / 2
        p3y = (polist[i][1] + polist[i + 1][1]) / 2

        deltax = p3x - p2x
        deltay = p3y - p2y
        
        #if length < 1e-12:
        #    print("Linie zu kurz, überspringe")
        #    i += 1
        #    continue
        #print("deltax/y", deltax, deltay)

        length = (deltax**2 + deltay**2)**0.5

        #90°-Drehung
        #dxf = x der senkrechten
        #dyf = y der senkrechten
        dxf = -deltay / length
        dyf = deltax / length
        
        #print("dxf,dyf", dxf, dyf)

        from scipy.optimize import root_scalar
        from shapely.geometry import Point

        basepoint = Point(p3x, p3y)

        nearby_buildings = building_gdf[
            building_gdf.geometry.distance(basepoint) <= 500#dynamic radius based on iteration is very very essential to implemnt
        ]

        print("basepoint koordiantes", basepoint)

        house_coords = [
            (point.x, point.y)
            for point in nearby_buildings.geometry
        ]
        print("house coordiantes", house_coords)
        if not house_coords:
            print("no nearby buildings")
            i = i + 1
            continue
            
        def houses_derivative(x):
            total = 0.0

            for dxn, dyn in house_coords:
                denominator = (
                    (dyf * x - (dyn - basepoint.y)) ** 2
                    + (dxf * x - (dxn - basepoint.x)) ** 2#weighted towards angle based on how many houses are affected MUST DO in final version
                ) ** 0.5

                if denominator > 1e-12:
                    total += (
                        dyf * (dyf * x - (dyn - basepoint.y))
                        + dxf * (dxf * x - (dxn - basepoint.x))
                    ) / denominator
                else:
                    print("bad")

            return total
        
        result = root_scalar(
            houses_derivative,
            bracket=[-10000, 10000],#THIS COULD BE DYNAMIc based off of p3 to p2 distance#this dynamic constrains the minimum to stay within houses-bound which is set by the iteration dynamic (currently linear 500m) as describet by a comment above
            method="brentq"#comment in the line above is improtant
        )

        x_zero = result.root

        print("Derivative zero at:", x_zero)
        print("Derivative zero at(brentq:", result)

        #ny = dyf * 2
        #nx = dxf * 2

        
        #delta_lon = x_zero * nx
        #delta_lat = x_zero * ny
        #delta_lon = x_zero * nx#wiaimmerummer
        #delta_lat = x_zero * ny

        
        #print("Verschiebugng", delta_lat, delta_lon)

        #finalx = p3x + delta_lon
        #finaly = p3y + delta_lat
        finalx = p3x + x_zero * dxf
        finaly = p3y + x_zero * dyf

        polist.insert(i + 1, (finalx, finaly))

        i = i + 2
        rangesetter = rangesetter + 1
        angleitera = angleitera + 1

    return polist
