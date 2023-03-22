import googlemaps

# Replace YOUR_API_KEY with your actual API key
gmaps = googlemaps.Client(key='AIzaSyDAIG_LIRSb693AN2kQqmGelUzWmTcwD14')
# Search for coffee shops in New York City
places_result = gmaps.places('coffee shop in New York City')

# Print the name and address of each coffee shop
for place in places_result['results']:
    print(place['name'])
    print(place['formatted_address'])
