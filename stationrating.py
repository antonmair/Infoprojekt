from shapely.geometry import Point
import math

def calc_station_rating(station_polist, building_gdf, search_radius=8001):
    #define station rating list
    station_rating = []
    
    #loop for every point
    for px, py in station_polist:
        basepoint = Point(px, py)

        #load nearby buildings from geodataframe
        nearby_buildings = building_gdf[
            building_gdf.geometry.distance(basepoint) <= search_radius
        ]

        #calculate rating per point
        rating = 0.0
        for geom in nearby_buildings.geometry:
            distance = geom.distance(basepoint)
            rating += search_radius - distance
        #
        station_rating.append(rating)

    #define station points
    station_points = []

    #defines threshold as only top 30% of locations
    threshold = sorted(station_rating)[int(0.7 * len(station_rating))]

    #requirements loop
    for i in range(1, len(station_rating) - 1):
        if (
            station_rating[i] > station_rating[i - 1]#local max before
            and station_rating[i] > station_rating[i + 1]#local max after
            and station_rating[i] > threshold#top30%
            and station_rating[i] > 50000 #total value, currently a really low bar can be changed to higher
        ):
            #add as preliminary station location
            candidate = station_polist[i]

            #not ideal because compares only to last generated station by direct distance
            if not station_points:
                station_points.append(candidate)
            else:
                last_x, last_y = station_points[-1]
                d = math.sqrt(
                    (candidate[0] - last_x) ** 2 +
                    (candidate[1] - last_y) ** 2
                )
                if d >= 600:
                    station_points.append(candidate)

    return station_points
