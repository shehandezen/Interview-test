    * | Python | Javascript | FastAPI | *
# 🗺 Nearest Location Finder 🗺
![Cover image](https://github.com/shehandezen/Nearest-location-finder/blob/main/cover.png?raw=true)
In here, I used a formula that can computes the square of the half-chord length between the points.

### The Haversine Formula

The formula is derived from the law of haversines, which relates the sides and angles of spherical triangles. It is expressed as:

![The haversine Formula](https://github.com/shehandezen/Nearest-location-finder/blob/main/formula.PNG?raw=true)

```
# calculate the distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
```

[Live App Here](https://nearest-location-finder-1.onrender.com)

[API Link Here](https://nearest-location-finder.onrender.com/location)
