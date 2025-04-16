import json
import eq_explore_data as eq
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Map the Earthquakes
# data = [Scattergeo(lon=lons, lat=lats)]

# OR

data = [{
    "type": "scattergeo",
    "lon": eq.lons,
    "lat": eq.lats,
    "text": eq.hover_texts,
    "marker": {
        'size': [5*mag for mag in eq.mags],
        'color': eq.mags,
        'colorscale': "Viridis",
        'reversescale': True,
        'colorbar': {'title': "Magnitude"},
    },
}]
my_layout = Layout(title="Global Earthquakes")
fig = {"data":data, "layout":my_layout}
offline.plot(fig, filename="global_earthquakes.html")