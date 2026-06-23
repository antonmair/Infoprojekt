from shapely.geometry import Point

def calc_station_rating(station_polist, building_gdf, search_radius=800):
    #print("i was here")
    station_rating = []

    for px, py in station_polist:
        basepoint = Point(px, py)

        nearby_buildings = building_gdf[
            building_gdf.geometry.distance(basepoint) <= search_radius
        ]

        rating = 0.0
        for geom in nearby_buildings.geometry:
            distance = geom.distance(basepoint)
            rating += search_radius - distance

        station_rating.append(rating)

    station_points = []

    if len(station_rating) >= 3:
        #threshold = 0.8 * max(station_rating)
        threshold = sorted(station_rating)[int(0.75 * len(station_rating))]#0.8 is dynamic evaluation of how many stations for smaller towns are relaly needed
        
        for i in range(1, len(station_rating) - 1):
            if (
                station_rating[i] > station_rating[i - 1]
                and station_rating[i] > station_rating[i + 1]
                and station_rating[i] > threshold
            ):
                station_points.append(station_polist[i])

    return station_points