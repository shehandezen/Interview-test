import sqlite3
import math
from fastapi import FastAPI

app = FastAPI()

# calculate the distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# find the nearest location 
def find_nearest_location(lat, lon):
    conn = sqlite3.connect('locations.sqlite')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM locations')
    locations = cursor.fetchall()
    conn.close()

    nearest_location = None
    shortest_distance = float('inf')
    country_In = None
    N_lat = float('inf')
    N_lon = float('inf')

    for location in locations:
        loc_name, loc_lat, loc_lon, country = location
        distance = haversine(float(lat), float(lon), float(loc_lat), float(loc_lon))
        if distance < shortest_distance:
            nearest_location = loc_name
            shortest_distance = distance
            country_In = country
            N_lat = loc_lat
            N_lon = loc_lon

    return nearest_location, shortest_distance, country_In, N_lat, N_lon

# Function to handle the button click in the GUI
def loc_search(lat,lon):
    try:
        nearest_location, distance, country, N_lat, N_lon  = find_nearest_location(float(lat), float(lon))
        return { 'status': 'success',
                 'data':{
                      'nearest_location': nearest_location, 
                      'distance': round(distance,2),
                      'country': country, 
                      'latitude': N_lat, 
                      'longitude': N_lon 
                      }
                }
    except ValueError:
        return { 'status': 'error', 
                'data':{
                    'error': "Invalid Input", 
                    'message': "Please enter valid numbers for latitude and longitude." 
                    }
                } 

@app.get("/location/{latitude}/{longitude}")
async def read_item(latitude: float, longitude:float ):
    print(latitude,longitude)
    return loc_search(float(latitude),float(longitude))