import requests
import os
from dotenv import load_dotenv
from datetime import datetime

from main import load_places

load_dotenv()

# Google Places API endpoint for Place Search
search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

details_url = "https://maps.googleapis.com/maps/api/place/details/json"

def get_opening_time(places, api_key, desired_date):
    print(f'Considered date {desired_date}')
    place_ids = []
    for place in places:
        params = {
            "input": f"{place['name']} {place['address']}",
            "inputtype": "textquery",
            "key": api_key,
        }
        response = requests.get(search_url, params=params)
        data = response.json()

        if "candidates" in data and len(data["candidates"]) > 0:
            place_id = data["candidates"][0]["place_id"]
            place_ids.append((place['name'],place['address']))
            details_params = {
            "place_id": place_id,
            "key": api_key,
            }
            details_response = requests.get(details_url, params=details_params)
            details_data = details_response.json()
            if "result" in details_data and "opening_hours" in details_data["result"]:
                opening_hours = details_data["result"]["opening_hours"]["periods"]

                desired_date_obj = datetime.strptime(desired_date, "%Y-%m-%d")
                
                for period in opening_hours:
                    if "open" in period and "close" in period:
                        open_day = period["open"]["day"]
                        close_day = period["close"]["day"]
                        if open_day <= close_day and open_day <= desired_date_obj.weekday() <= close_day:
                            open_time = period["open"]["time"][:-2]
                            close_time = period["close"]["time"][:-2]
                            print(f"{place['name']} \t from {open_time} to {close_time}")

        else:
            print(f"Place {place['name']} at {place['address']} not found")
    return place_ids

if __name__ == "__main__":
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    file_path = os.getenv("FILE_PATH")
    origin = os.getenv("ORIGIN")
    origin_place = {"city": origin.split(',')[1], "address": origin.split(',')[0], "name": ''}
    desired_date = "2023-08-19"
    
    if not api_key:
        raise ValueError("Google Maps API key is missing. Set it in the --api_key argument or in the .env file.")

    if not file_path:
        raise ValueError("File path is missing. Set it in the --file_path argument or in the .env file.")

    places = load_places(file_path)
    print(get_opening_time(places, api_key, desired_date))