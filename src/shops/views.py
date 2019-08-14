import requests
import json
import urllib3
from urllib.parse import quote
from urllib.parse import urlencode
from django.shortcuts import render
from django.conf import settings

# Create your views here.

# YELP API KEY & HOST
YELP_API_KEY = settings.YELP_SECRET_KEY
YELP_API_HOST = 'https://api.yelp.com/v3/'

# YELP API PATHS
SEARCH_PATH = 'businesses/search/'
BUISNESS_PATH = 'business/' # Business ID will go after slash

# DEFAULTS
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 5

def request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{}{}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer {}'.format(str(api_key))
    }
    r = requests.get(url, headers=headers, params=url_params)
    return r.json()

def get_business(api_key, business_id):
    buisness_path = BUSINESS_PATH + business_id
    return request(API_HOST, buisness_path, YELP_API_KEY)

def search(api_key, location):
    url_params = {
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, YELP_API_KEY, url_params=url_params)

def shops_view(request):

    return render(request, 'shops.html', {})
