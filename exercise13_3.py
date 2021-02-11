# Import library needed
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# API key confirmation
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Input location
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # Using maps API to find the location
    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    # Parsing json data from url
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # Conditional if there is no data retrieved
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # Checking the json dump
    print(json.dumps(js, indent=4))

    # Retrieving the place id from the data
    placeid = js['results'][0]['place_id']
    print('Place id:', placeid)
    location = js['results'][0]['formatted_address']
    print(location)
