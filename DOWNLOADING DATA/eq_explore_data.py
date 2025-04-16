import json


# Explore the structure of the data
# filename = "data/earthquake/eq_data_1_day_m1.json"
filename = "data/earthquake/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = "data/earthquake/readable_eq_data.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent=4)

"""
# Without list comprehension
all_eq_dicts = all_eq_data["features"]

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    title = eq_dict["properties"]["title"]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)"""

# using list comprehension
all_eq_dicts = all_eq_data["features"]

mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts]

# print(mags[:10])
# print(lons[:10])