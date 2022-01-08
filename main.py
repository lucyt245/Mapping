import folium
import pandas

map = folium.Map(location = [55, -4.4], zoom_start = 6, tiles = 'Stamen Terrain')
data = pandas.read_csv('volcanoes.txt')

fg = folium.FeatureGroup(name = 'MyMap')

lat = list(data['LAT'])
lon = list(data['LON'])
volc_name = list(data['NAME'])
location = list(data['LOCATION'])

for lt, ln, nm, loc in zip(lat, lon, volc_name, location):
    loc = loc[3:]
    # gets rid of the 'US-' part of the location
    marker = nm + ', ' + loc
    fg.add_child(folium.Marker(location = [lt, ln], popup = marker, icon = folium.Icon(color = 'red')))

map.add_child(fg)

map.save('firstMap.html')
