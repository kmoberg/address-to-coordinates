import requests
import json
import csv


# Begin by getting the Google Maps API key. You can get this by going to: https://developers.google.com/maps/gmp-get-started
f = open("maps_api_key.txt", "r")
apiKey = f.read()
f.close

inputFile = "addresses.csv"

# Convert the input location to coordinates, using the geocode Maps API.


def Get_Coordinates(apiKey, address):

    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ', '+'), apiKey))
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        # Dig down into the JSON objects to find the lat
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        # Then the lng (long)
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    except:
        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    return lat, lng


with open(inputFile, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

        lat, lng = Get_Coordinates(apiKey, row)
        print(lat, lng)
