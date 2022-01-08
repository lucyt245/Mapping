import folium
import pandas

map = folium.Map(location = [55, -4.4], zoom_start = 6, tiles = 'Stamen Terrain')
data = pandas.read_csv('volcanoes.txt')

def location_checker(loc):
    if loc[:3] == 'US-':
        return loc[3:]
    else:
        return loc

fg_volc = folium.FeatureGroup(name = 'Volcano')
fg_pop = folium.FeatureGroup(name = 'Population')

lat = list(data['LAT'])
lon = list(data['LON'])
volc_name = list(data['NAME'])
location = list(data['LOCATION'])
# turns data from 'volcanoes.txt' into a list format

for lt, ln, nm, loc in zip(lat, lon, volc_name, location):
    # places markers on volcano locations in USA
    loc = location_checker(loc)
    # gets rid of the 'US-' part of the location
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
