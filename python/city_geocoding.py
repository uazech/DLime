# %%
import pandas as pd
import googlemaps
API_KEY = "YOUR_API_KEY"
# %%
gmaps = googlemaps.Client(key=API_KEY)
df = pd.read_csv("KaggleV2-May-2016.csv")
df.head()
# %%
data = []
for place in df.Neighbourhood.unique():

    print(place)
    try:
        geocode_result = gmaps.geocode(place + " Espirito Santo")
        loc = geocode_result[0]["geometry"]["location"]
        data.append([place, loc['lat'], loc['lng']])
    except:
        print("error")
# %%
locs = pd.DataFrame(data)
locs.columns = ["place", "lat", "lng"]


locs.to_csv("data/place.csv")
locs.head()


# %%
