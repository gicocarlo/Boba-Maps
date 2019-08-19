from django.shortcuts import render
from django.conf import settings
from django.http import Http404
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
SEARCH_LIMIT = 5

def request(host, path, api_key, params=None):
    params = params or {}
    url = '{}{}'.format(host,path)
    headers = {
        'Authorization': 'bearer %s' % YELP_API_KEY
    }
    response = requests.get(url=url, params=params, headers=headers)
    return response.json()

def search_boba(path, api_key, location):
    params = {
        'categories': 'bubbletea',
        'location': location,
        'limit': SEARCH_LIMIT
    }
    return request(YELP_API_HOST, path, api_key, params)

def get_boba_spot(api_key, business_id):
    business_path = BUSINESS_PATH + business_id
    return request(YELP_API_HOST, business_path, api_key)

def boba_shops_id(location):
    b = search_boba(SEARCH_PATH, YELP_API_KEY, location)
    b_list = b['businesses']
    b_list_id = []
    for i in range(len(b_list)):
        b_list_id.append(b_list[i]['id'])
    return b_list_id

def boba_shops(location):
    boba_list = []
    b_list_id = boba_shops_id(location)
    for i in b_list_id:
        response = get_boba_spot(YELP_API_KEY, i)
        boba_shop = {
            'name': response["name"],
            'url': response["url"],
            'addresses': response["location"]["address1"],
            'rating': response["rating"]
        }
        boba_list.append(boba_shop)

    return boba_list

def shops_view(request):
    try:
        if request.method == 'GET':
            address = request.GET.get('address')
            boba_list = boba_shops(address)
            boba_dict = {'boba_list': boba_list}
        return render(request, 'shops.html', boba_dict)
    except:
        raise Http404("Page does not exist")
