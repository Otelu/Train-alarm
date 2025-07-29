import googlemaps
from datetime import datetime
import time
import math

# Replace 'YOUR_API_KEY' with your actual API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Define your starting point and destination
start_point = "Start Address"
end_point = "Destination Address"
alarm_radius = 5  # in kilometers

# Calculate distance between two points using Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# Request directions
def get_current_location_along_route():
    try:
        # Request directions
        directions = gmaps.directions(start_point, end_point)

        # Extract current location (assuming you're following the first route)
        current_location = directions[0]['legs'][0]['steps'][0]['start_location']

        # Extract latitude and longitude
        latitude = current_location['lat']
        longitude = current_location['lng']

        return latitude, longitude
    except Exception as e:
        print("Error:", e)
        return None

# Main function to track the current location along the route
def track_location_along_route():
    while True:
        location = get_current_location_along_route()
        if location:
            print("Current Location: Latitude {}, Longitude {}".format(*location))
            # Calculate distance to destination
            destination_lat, destination_lon = gmaps.geocode(end_point)[0]['geometry']['location']
            distance_to_destination = haversine(location[0], location[1], destination_lat, destination_lon)
            print("Distance to destination:", distance_to_destination)
            # Check if within alarm radius
            if distance_to_destination <= alarm_radius:
                print("Alarm! You are within {} km of your destination.".format(alarm_radius))
                # You can trigger any alarm mechanism here
                # For example, you could play a sound or send a notification
                # Replace the print statement above with the desired alarm mechanism
        else:
            print("Unable to retrieve location.")
        # Wait for a certain amount of time before checking again
        # Adjust this according to your needs
        time.sleep(60)

if __name__ == "__main__":
    track_location_along_route()
