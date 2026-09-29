import geopandas as gpd
from shapely.geometry import Point

def site_frame(lat: float, lon: float):
    return gpd.GeoDataFrame({"site":["candidate"]},geometry=[Point(lon,lat)],crs="EPSG:4326")
