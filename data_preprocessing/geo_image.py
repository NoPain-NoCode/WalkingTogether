import geopandas as gpd
import folium
from shapely import geometry

road_file = "C:\\Users\\DY\Documents\\WalkingTogether\\data_preprocessing\\raw_data\\걷고싶은서울길_Shape\\둘레길\\폴리라인\\둘레길_polyline.shp"
road = gpd.read_file(road_file, encoding='utf-8')

print(road)
cities = road[road.Id=="0"]




m = folium.Map(
    location = [37.46715465768088, 126.94819572254312],
    tiles = 'Stamen Terrain',
    zoom_start = 7
)

folium.PolyLine(
    locations = cities,
    tooltip='PolyLine'
).add_to(m)
