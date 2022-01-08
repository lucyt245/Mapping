import folium
import pandas

map = folium.Map(location = [55, -4.4], zoom_start = 6, tiles = 'Stamen Terrain')
data = pandas.read_csv('volcano.csv')

fg_volc = folium.FeatureGroup(name = 'Volcano')
fg_pop = folium.FeatureGroup(name = 'Population')

lat = list(data['Latitude'])
lon = list(data['Longitude'])
location = list(data['Country'])
volc_name = list(data['V_Name'])
risk = list(data['risk'])

for lt, ln, nm, loc, rsk in zip(lat, lon, volc_name, location, risk):
    # places markers on volcano locations worldwide
    if str(rsk) != 'nan':
        # only volcanoes that have some semblenece of activity - otherwise it's just a fancy mountain
        marker = nm + ' (' + loc + ')'
        fg_volc.add_child(folium.Marker(location = [lt, ln], fill = True, icon = folium.Icon(color = 'red'),
        popup = marker))

fg_pop.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'}))
# creates polygons for countries - colour based on population

map.add_child(fg_volc)
map.add_child(fg_pop)
map.add_child(folium.LayerControl())
map.save('firstMap.html')
