import folium

map = folium.Map(location = [55, -4.4], zoom_start = 6, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name = 'MyMap')

for coordinates in [[31, 5],[50, 10]]:
    fg.add_child(folium.Marker(location = coordinates, popup = 'marker', icon = folium.Icon(color = 'purple')))

map.add_child(fg)

map.save('firstMap.html')
