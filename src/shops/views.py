from django.shortcuts import render
from django.conf import settings
import requests
import json

# Create your views here.

def request(host, path, api_key, url_params=None):
    
    return request.get()

def search():
    pass

def get_business():
    pass

def query_api():
    pass

def shops_view(request):
    # YELP_API_KEY = settings.YELP_SECRET_KEY
    # YELP_API_HOST = 'https://api.yelp.com/v3/'
    # SEARCH_PATH = 'businesses/search/'
    # BUISNESS_PATH = 'business/' # Business ID will go after slash
    return render(request, 'shops.html', {})
