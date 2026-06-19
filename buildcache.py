import osmnx as ox
import geopandas as gpd
from geopy.distance import geodesic

building_gdf_wgs84 = None
building_gdf_local = None
#building_sindex = None

#downloads buildings around midpoint(point2, point3) and creates a GeoDataFrame and spatial index
def building_cache(point2, point3, target_crs):
    global building_gdf_wgs84, building_gdf_local#, building_sindex

    #midpoint of line
    mid_lat = (point2[0] + point3[0]) / 2
    mid_lon = (point2[1] + point3[1]) / 2

    #distance in meters
    dist = geodesic(point2, point3).meters
    
    #circle (or square?) around midpoint
    radius = dist * 0.6#1 is safer but slower

    #download osm
    try:
        building_gdf_wgs84 = ox.features_from_point(
            (mid_lat, mid_lon),
            tags={"building": True},
            dist=radius
        )
    except Exception:
        building_gdf_wgs84 = gpd.GeoDataFrame(
            geometry=[],
            crs="EPSG:4326"
        )

    #convert to allowed geometry types
    building_gdf_wgs84 = building_gdf_wgs84[
        building_gdf_wgs84.geometry.type.isin(
            ["Point", "Polygon", "MultiPolygon"]
        )
    ].copy()

    #convert polygons to centroids
    building_gdf_wgs84["geometry"] = building_gdf_wgs84.geometry.apply(
        lambda g: g.centroid if g.geom_type in ["Polygon", "MultiPolygon"] else g
    )

    #local projected version for calculations
    building_gdf_local = building_gdf_wgs84.to_crs(target_crs)

    #create spatial index
    #building_sindex = building_gdf_local.sindex

    return mid_lat, mid_lon, radius
