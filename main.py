import googlemaps
import os
from dotenv import load_dotenv
from urllib.parse import quote
# Load environment variables from .env file
load_dotenv()

def load_places(file_path):
    places = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        city = ""
        for line in lines:
            line = line.strip()
            if line:
                if line.isupper():
                    city = line
                else:
                    place = {"city": city, "name": "", "address": ""}
                    parts = line.split('-', 1)
                    if len(parts) == 2:
                        place["name"] = parts[0].split('.')[1].strip()
                        place["address"] = parts[1].strip()
                        places.append(place)
    
    return places


def calculate_route(origin ,places, api_key):
    gmaps = googlemaps.Client(key=api_key)
    waypoints = [place["name"] + ' ' + place["address"] + ' ' + place["city"] for place in places]
    print('waypoints',waypoints)
    directions_result = gmaps.directions(
        origin=origin,
        destination=origin,
        waypoints=waypoints,
        optimize_waypoints=True,  
        mode="walking" 
    )
    encoded_polyline = directions_result[0]['waypoint_order']
    return encoded_polyline

if __name__ == "__main__":
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    file_path = os.getenv("FILE_PATH")
    origin = os.getenv("ORIGIN")
    origin_place = {"city": origin.split(',')[1], "address": origin.split(',')[0], "name": ''}
    
    if not api_key:
        raise ValueError("Google Maps API key is missing. Set it in the --api_key argument or in the .env file.")

    if not file_path:
        raise ValueError("File path is missing. Set it in the --file_path argument or in the .env file.")

    places = load_places(file_path)
    
    waypoints_order = calculate_route(
        origin,
        places,
        api_key
    )
    waypoints = [origin_place] + [places[waypoint_index] for waypoint_index in waypoints_order] + [origin_place]

    print('waypoints_order',waypoints)
    # Construct the Google Maps URL with ordered waypoints
    places_addresses = [(place["name"] +' '+  place["address"] + ' ' + place["city"]).replace(' ', '+') for place in waypoints]
    google_maps_url = f"https://www.google.com/maps/dir/{'/'.join(places_addresses)}"
    print("Google Maps URL with optimized route:\n", google_maps_url)
