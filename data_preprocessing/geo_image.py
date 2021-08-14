import geopandas as gpd
import folium
from shapely import geometry
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser

dr_file = "C:\\Users\\DY\Documents\\WalkingTogether\\data_preprocessing\\raw_data\\걷고싶은서울길_Shape\\둘레길\\폴리라인\\둘레길_polyline.shp"
stmh_file = "C:\\Users\\DY\Documents\\WalkingTogether\\data_preprocessing\\raw_data\\걷고싶은서울길_Shape\\생태문화길\\폴리라인\\생태문화길_polyline.shp"
sk_file = "C:\\Users\\DY\Documents\\WalkingTogether\\data_preprocessing\\raw_data\\걷고싶은서울길_Shape\\성곽길\\폴리라인\\성곽길_polyline.shp"
zr_file = "C:\\Users\\DY\Documents\\WalkingTogether\\data_preprocessing\\raw_data\\걷고싶은서울길_Shape\\자락길\\폴리라인\\자락길_polyline.shp"
dp_file = "C:\\Users\\DY\Documents\\WalkingTogether\\data_preprocessing\\raw_data\\걷고싶은서울길_Shape\\한강지천길_계절길\\단풍길\\단풍길_polyline.shp"
bk_file = "C:\\Users\\DY\Documents\\WalkingTogether\\data_preprocessing\\raw_data\\걷고싶은서울길_Shape\\한강지천길_계절길\\봄꽃길\\봄꽃길_polyline.shp"
hkzc_file = "C:\\Users\\DY\Documents\\WalkingTogether\\data_preprocessing\\raw_data\\걷고싶은서울길_Shape\\한강지천길_계절길\\한강지천길\\한강지천길_polyline.shp"

dr = gpd.read_file(dr_file, encoding='utf-8')
stmh = gpd.read_file(stmh_file, encoding='utf-8')
sk = gpd.read_file(sk_file, encoding='utf-8')
zr = gpd.read_file(zr_file, encoding='utf-8')
dp = gpd.read_file(dp_file, encoding='utf-8')
bk = gpd.read_file(bk_file, encoding='utf-8')
hkzc = gpd.read_file(hkzc_file, encoding='utf-8')



# print(dr)
# cities = dr[dr.Name== b'???????\xc2\xcb?']

m = folium.Map(
    location = [37.46715465768088, 126.94819572254312],
    tiles = 'Stamen Terrain',
    zoom_start = 7
)

# # 이렇게 선만 표현하는 건 가능하긴 함....
# ax = dr.plot(color='purple')
# ax.set_axis_off()
# plt.show()

# print("cities")
# print(cities)

dr_geo = 'C:\\Users\\DY\\Documents\\WalkingTogether\\data_preprocessing\\data\\둘레길_polyline.json'

folium.PolyLine(
    locations = dr_geo,
    tooltip='PolyLine'
).add_to(m)
