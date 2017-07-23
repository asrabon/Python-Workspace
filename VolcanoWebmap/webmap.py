import folium
import pandas

volcanoes = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[volcanoes['LAT'].mean(), volcanoes['LON'].mean()],zoom_start=8,tiles='Mapbox bright')

#determines what color the icon of the marker should be dependent on the elevation
def determineIconColor(elev):
    minimum = int(min(volcanoes['ELEV']))
    step = int((max(volcanoes['ELEV']) - minimum)/3)
    if elev in range(minimum,minimum+step):
        return 'green'
    elif elev in range(minimum+step,minimum+step*2):
        return 'orange'
    else:
        return 'red'

def determineFillColor(x):
    if x <= 10000000:
        return 'green'
    elif x <= 20000000:
        return 'orange'
    else:
        return 'red'

fg=folium.FeatureGroup(name="Volcano Locations")

for lat,lon,name,elev in zip(volcanoes['LAT'],volcanoes['LON'],volcanoes['NAME'],volcanoes['ELEV']):
    fg.add_child(folium.Marker(location=[lat,lon] , popup=name, icon=folium.Icon(color=determineIconColor(elev),icon_color='black')))
map.add_child(fg, name=None, index=None)

map.add_child(folium.GeoJson(data = open("worldPopulation.json"), name="World Population",
style_function=lambda x: {'fillColor':determineFillColor(x['properties']['POP2005'])}))

map.add_child(folium.LayerControl())

map.save(outfile="test.html", close_file=True)
