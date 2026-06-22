import osmnx as ox
import geopandas as gpd
import pandas as pd
from geopy.distance import geodesic
from shapely.geometry import Point

building_gdf_wgs84 = None
building_gdf_local = None
cache_gdf_wgs84 = None
cache_gdf_local = None
cache_sindex = None
cache_coverage_local = None

def building_cache(point2, point3, target_crs):
    global building_gdf_wgs84, building_gdf_local
    global cache_gdf_wgs84, cache_gdf_local, cache_sindex, cache_coverage_local

    # midpoint of line
    mid_lat = (point2[0] + point3[0]) / 2
    mid_lon = (point2[1] + point3[1]) / 2

    # distance in meters
    dist = geodesic(point2, point3).meters

    # search radius
    radius = dist * 0.6

    # current request center as GeoSeries
    center_wgs84 = gpd.GeoSeries(
        [Point(mid_lon, mid_lat)],
        crs="EPSG:4326"
    )
    center_local = center_wgs84.to_crs(target_crs)
    center_point_local = center_local.iloc[0]

    # circular requested area in local CRS
    request_area_local = center_point_local.buffer(radius)

    # check whether requested area is already fully covered by cache
    covered_by_cache = False
    if cache_coverage_local is not None:
        covered_by_cache = cache_coverage_local.covers(request_area_local)

    # only call OSM if the requested area is not yet covered
    if not covered_by_cache:
        try:
            new_gdf_wgs84 = ox.features_from_point(
                (mid_lat, mid_lon),
                tags={"building": True},
                dist=radius
            )
        except Exception:
            new_gdf_wgs84 = gpd.GeoDataFrame(
                geometry=[],
                crs="EPSG:4326"
            )

        # keep only supported geometry types
        new_gdf_wgs84 = new_gdf_wgs84[
            new_gdf_wgs84.geometry.type.isin(
                ["Point", "Polygon", "MultiPolygon"]
            )
        ].copy()

        # convert polygons to centroids
        new_gdf_wgs84["geometry"] = new_gdf_wgs84.geometry.apply(
            lambda g: g.centroid if g.geom_type in ["Polygon", "MultiPolygon"] else g
        )

        # convert to local CRS
        new_gdf_local = new_gdf_wgs84.to_crs(target_crs)

        # append to global cache
        if cache_gdf_wgs84 is None:
            cache_gdf_wgs84 = new_gdf_wgs84.copy()
            cache_gdf_local = new_gdf_local.copy()
        else:
            cache_gdf_wgs84 = gpd.GeoDataFrame(
                pd.concat([cache_gdf_wgs84, new_gdf_wgs84], ignore_index=True),
                crs="EPSG:4326"
            )
            cache_gdf_local = gpd.GeoDataFrame(
                pd.concat([cache_gdf_local, new_gdf_local], ignore_index=True),
                crs=target_crs
)
            # remove duplicate buildings if same OSM object appears multiple times
            cache_gdf_wgs84 = cache_gdf_wgs84.drop_duplicates()
            cache_gdf_local = cache_gdf_local.drop_duplicates()

        # rebuild spatial index on full cache
        cache_sindex = cache_gdf_local.sindex

        # extend covered area
        if cache_coverage_local is None:
            cache_coverage_local = request_area_local
        else:
            cache_coverage_local = cache_coverage_local.union(request_area_local)

    # if cache is still empty, return empty result
    if cache_gdf_local is None or len(cache_gdf_local) == 0:
        building_gdf_local = gpd.GeoDataFrame(geometry=[], crs=target_crs)
        building_gdf_wgs84 = gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
        return mid_lat, mid_lon, radius

    # spatial-index preselection by bounding box
    candidate_idx = list(cache_sindex.intersection(request_area_local.bounds))
    candidate_local = cache_gdf_local.iloc[candidate_idx].copy()

    # exact filtering to circle
    candidate_local = candidate_local[
        candidate_local.geometry.distance(center_point_local) <= radius
    ].copy()

    building_gdf_local = candidate_local
    building_gdf_wgs84 = candidate_local.to_crs("EPSG:4326")

    return mid_lat, mid_lon, radius
