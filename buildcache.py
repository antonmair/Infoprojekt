import osmnx as ox
import geopandas as gpd
from shapely.geometry import Point
from geopy.distance import geodesic

building_gdf = None
building_sindex = None

#downloads buildings around midpoint(point2, point3) and creates a GeoDataFrame and spatial index
def building_cache(point2, point3):
    global building_gdf, building_sindex

    #midpoint of line
    mid_lat = (point2[0] + point3[0]) / 2
    mid_lon = (point2[1] + point3[1]) / 2

    #distance in meters
    dist = geodesic(point2, point3).meters

    #circle (or square?) around midpoint
    radius = dist * 1 #varible for range of downloaded housees (times 3 or 4 on serious)

    #download osm
    try:
        building_gdf = ox.features_from_point(
            (mid_lat, mid_lon),
            tags={"building": True},
            dist=radius
        )
    except Exception:#dont like this change...
        building_gdf = gpd.GeoDataFrame(
            geometry=[],
            crs="EPSG:4326"
        )   
    #convert to centroid
    building_gdf = building_gdf[
        building_gdf.geometry.type.isin(
            ["Point", "Polygon", "MultiPolygon"]
        )
    ]
    building_gdf["geometry"] = building_gdf.geometry.apply(
        lambda g: g.centroid
        if g.geom_type in ["Polygon", "MultiPolygon"]
        else g
    )

    #create spatial index
    building_sindex = building_gdf.sindex

    #print(f"Cached {len(building_gdf)} buildings")