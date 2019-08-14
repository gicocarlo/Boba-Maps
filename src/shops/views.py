from django.shortcuts import render
from django.conf import settings
import requests
import json

# Create your views here.

# YELP API KEY & HOST
YELP_API_KEY = settings.YELP_SECRET_KEY
YELP_API_HOST = 'https://api.yelp.com/v3'

# YELP API PATHS
SEARCH_PATH = '/businesses/search'
BUSINESS_PATH = '/businesses/' #ID

# DEFAULTS
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 3

def request(host, path, api_key, params=None):
    params = params or {}
    url = '{}{}'.format(host,path)
    headers = {
        'Authorization': 'bearer %s' % YELP_API_KEY
    }
    response = requests.get(url=url, params=params, headers=headers)
    return response.json()

def search(path, api_key):
    params = {
        'categories': 'bubbletea',
        'location': DEFAULT_LOCATION,
        'limit': SEARCH_LIMIT
    }
    return request(YELP_API_HOST, path, api_key, params)

def get_business(api_key, business_id):
    business_path = BUSINESS_PATH + business_id
    return request(YELP_API_HOST, business_path, api_key)

def shops_view(request):
    b = search(SEARCH_PATH, YELP_API_KEY)
    bus_id = b['businesses'][2]['id']
    # print(bus_id)
    response = get_business(YELP_API_KEY, bus_id)
    # print(businesses)
    return render(request, 'shops.html', response)
