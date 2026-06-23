from spawnerhouse import spawnerh
import geopandas as gpd
from shapely.geometry import Point
from ipyleaflet import Polyline

def curvecreatorh(polist, building_gdf, angle_weight, first_value, second_value, status, radius, m, utm_crs, show_temp_line):
    #define amunt of iterations
    radius = radius/0.6*2

    #dynamic iteration count between 1 and 50km
    min_radius = 1000 #1 km
    max_radius = 50000 #50 km
    min_iter = 6
    max_iter = 11
    
    if radius <= min_radius:
        iternumber = min_iter
    elif radius >= max_radius:
        iternumber = max_iter
    else:
        t = (radius - min_radius) / (max_radius - min_radius)
        iternumber = round(min_iter + t * (max_iter - min_iter)) 

    #increased iterations for indirect curves because of longer lines
    if angle_weight <= 500:
        iternumber = iternumber +1
    if angle_weight <= 50:
        iternumber = iternumber +1
        
    #iternumber = 12 #old static iteration counter
    
    #define temporary iteration line
    temp_line = None
    
    #define station polist
    station_polist = None

    #generate temporary lines every iteration
    if show_temp_line:
        temp_line = Polyline(
            locations=[],
            color="#85082b",
            weight=3,
            fill=False
        )
        m.add_layer(temp_line)
    
    #main loop
    for k in range(int(iternumber)):
        #updated status
        status.value = f"<b style='color: green;'>Erstelle Trasse: {k}/{iternumber}</b>"
        
        #insert and move points
        polist = spawnerh(polist, k, building_gdf,angle_weight,first_value,second_value)
        
        #generate station_polist
        if len(polist) > 11 and station_polist == None:
            #calculate distance between random midpoints
            x10, y10 = polist[10]
            x11, y11 = polist[11]
            station_distance = ((x11 - x10)**2 + (y11 - y10)**2)**0.5

            #if this distance is lower that 20 or we are on the last iterations create station_polist with current points
            if station_distance < 20 or k == iternumber-1:
                station_polist = polist.copy()

        #update temporary line
        if show_temp_line:
            lineploth_wgs84 = gpd.GeoSeries(
                [Point(x, y) for x, y in polist],
                crs=utm_crs
            ).to_crs("EPSG:4326")

            temp_line.locations = [(geom.y, geom.x) for geom in lineploth_wgs84]
            
    return polist, station_polist
