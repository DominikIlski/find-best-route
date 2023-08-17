# Coffee Race Planner

This repository contains two Python scripts for planning a coffee race by optimizing a route and retrieving opening hours of coffee shops using the Google Maps and Places APIs.

## Requirements

- Python 3.x
- Google Maps API key
- `requests` library (`pip install requests`)
- `googlemaps` library (`pip install -U googlemaps`)
- `dotenv` library (`pip install python-dotenv`)

## Getting Started

1. Clone this repository to your local machine.

2. Rename the `.env.example` file to `.env` and update the values with your Google Maps API key, file path, and origin.

3. Create a text file named `places.txt` and add the list of coffee shop names and addresses.

4. Open a terminal and navigate to the directory containing the scripts.

5. Run the `main.py` script to calculate the optimized route and generate a Google Maps URL:

`python main.py`


6. Run the `open_time.py` script to retrieve opening hours for the specified date:

`python open_time.py`

## Scripts

### main.py

This script calculates an optimized route for a coffee race using the Google Maps API. It reads coffee shop names and addresses from a file, calculates the route, and generates a Google Maps URL.

**Usage:**
1. Provide your Google Maps API key, file path, and origin in the `.env` file.
2. Update the `places.txt` file with the list of coffee shop names and addresses.
3. Run the script:

`python main.py --api_key API_KEY --file_path places.txt`


### open_time.py

This script retrieves opening hours for coffee shops using the Google Places API. It reads coffee shop names and addresses from a file, queries the API for opening hours, and prints the results.

**Usage:**
1. Provide your Google Maps API key, file path, and origin in the `.env` file.
2. Update the `places.txt` file with the list of coffee shop names and addresses.
3. Run the script:
`python open_time.py`


## Notes

- The provided `.env` file should be updated with your actual API key, file path, and origin.
- Ensure that the required libraries are installed using `pip`.
- The opening hours retrieval is based on regular opening hours and may not include special dates or exceptions.

