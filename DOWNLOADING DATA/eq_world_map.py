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
    "lat": eq.lats
}]
my_layout = Layout(title="Global Earthquakes")
fig = {"data":data, "layout":my_layout}
offline.plot(fig, filename="global_earthquakes.html")
