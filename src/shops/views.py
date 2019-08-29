from django.shortcuts import render
from django.conf import settings
from django.http import Http404
import requests
import json

# YELP API KEY & HOST
# https://www.yelp.com/developers/documentation/v3/get_started

YELP_API_KEY = settings.YELP_SECRET_KEY
YELP_API_HOST = 'https://api.yelp.com/v3'

# YELP API PATHS

SEARCH_PATH = '/businesses/search'
BUSINESS_PATH = '/businesses/' #ID

# Search limit for number of bubble tea shops

SEARCH_LIMIT = 5

'''
request()

Given the YELP_API_KEY, send a get request to the API

Args:
    path (str): The path of the API after the domain
    params (dict)(optional): A set of query parameters in the request

Returns:
    dict: The JSON response from the request
'''

def request(path, params=None):
    params = params or {}
    url = '{}{}'.format(YELP_API_HOST, path)
    headers = {
        'Authorization': 'bearer %s' % YELP_API_KEY
    }
    response = requests.get(url=url, params=params, headers=headers)
    return response.json()

'''
search_boba()

Query the Search API by bubble tea shops, location and search limit to get the
closest shops in a given area

https://www.yelp.com/developers/documentation/v3/business_search

Args:
    path (str): The path of the API after the domain
    location (str): The user input where they want to find the closest shops

Returns:
    dict: the JSON response from the request
'''

def search_boba(path, location):
    params = {
        'categories': 'bubbletea',
        'location': location,
        'limit': SEARCH_LIMIT
    }
    return request(path, params)

'''
get_boba_spot()

Query the Business API by the business ID of a bubble tea shop. Returns more
information about the business

https://www.yelp.com/developers/documentation/v3/business

Args:
    business_id (str): The ID of the bubble tea shop to query

Returns:
    dict: The JSON response from the request
'''

def get_boba_spot(business_id):
    business_path = BUSINESS_PATH + business_id
    return request(business_path)

'''
boba_shops_id()

Calls search_boba() and for each bubble tea shop, get it's business ID

Args:
    location (str): The user input where they want to find the closest shops

Returns:
    boba_list_id (list): List of bubble tea shop business IDs
'''

def boba_shops_id(location):
    bubble_tea_shops = search_boba(SEARCH_PATH, location)
    boba_list = bubble_tea_shops['businesses']
    boba_list_id = []
    for i in range(len(boba_list)):
        boba_list_id.append(boba_list[i]['id'])
    return boba_list_id

'''
boba_shops()

Calls boba_shops_id() to get list of business IDs. For each business,
call get_boba_spot() to get rich info on each shop and add into a
dictionary [boba_shop]. Append each boba shop into a list [boba_list]. Each
element in the list represents an object (a bubble tea shop)

Args:
    location (str): The user input where they want to find the closest shops

Returns:
    boba_list (list): List of objects (bubble tea shops)
'''

def boba_shops(location):
    boba_list = []
    boba_list_id = boba_shops_id(location)
    for i in boba_list_id:
        response = get_boba_spot(i)
        boba_shop = {
            'name': response["name"],
            'url': response["url"],
            'address': response["location"]["address1"],
            'city': response["location"]["city"],
            'state': response["location"]["state"],
            'zip_code': response["location"]["zip_code"],
            'rating': response["rating"],
            'phone': response["display_phone"],
            'review_count': response["review_count"],
            'is_open_now': response["hours"][0]["is_open_now"],
            'photo': response["image_url"],
            'coordinates': response["coordinates"]
        }
        boba_list.append(boba_shop)

    return boba_list

'''
shops_view()

Gets input location from user and calls boba_shops() via GET request. Passes
list of bubble tea objects & location into a dictionary [boba_dict]. This will
then be rendered to shops.html

Args:
    request: A GET request that takes in the input from either the navigation
             bar or home page.

Return:
    render: Renders the shop page with data from the Yelp API

Raises:
    Http404: Any invalid data will cause a 404
'''

def shops_view(request):
    try:
        if request.method == 'GET':
            address = request.GET.get('address')
            boba_list = boba_shops(address)
            boba_dict = {
                'boba_list': boba_list,
                'location': address
            }
        return render(request, 'shops.html', boba_dict)
    except:
        raise Http404('Page does not exist')
