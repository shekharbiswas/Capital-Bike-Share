from uszipcode import SearchEngine, SimpleZipcode, Zipcode
import googlemaps
from datetime import datetime


def sample(x,y):
    return (x+y)

def get_zip(place_name):
    api_key = 'AIzaSyA3kI2g_PpuLcXj2V_xd5p_oPYtumZG43U'
    gmaps = googlemaps.Client(key=api_key)
    # Geocoding an address
    geocode_result = gmaps.geocode(place_name)
    try:
        zipcode = int(geocode_result[0]['address_components'][5]['long_name'])
        return zipcode
    except:
        return None

def get_population(zip):
    ## Get Zipcoe information
    search = SearchEngine()
    return search.by_zipcode(zip)