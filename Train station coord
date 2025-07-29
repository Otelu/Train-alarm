import googlemaps

# Replace 'YOUR_API_KEY' with your actual API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

def get_coordinates(address):
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print("No results found for address:", address)
            return None
    except Exception as e:
        print("Error:", e)
        return None

def select_railway_station(prompt):
    while True:
        address = input(prompt)
        coordinates = get_coordinates(address)
        if coordinates:
            return coordinates
        else:
            print("Please enter a valid address.")

if __name__ == "__main__":
    print("Welcome to the Railway Station Selector!")
    print("Please select your start and destination railway stations.")

    start_station = select_railway_station("Enter the address of your start railway station: ")
    destination_station = select_railway_station("Enter the address of your destination railway station: ")

    print("Start Station Coordinates:", start_station)
    print("Destination Station Coordinates:", destination_station)
