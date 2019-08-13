from django.shortcuts import render
from django.conf import settings

# Create your views here.

# shops_view()
def shops_view(request):
    # YELP_API_KEY = settings.YELP_SECRET_KEY
    # YELP_API_HOST = 'https://api.yelp.com/v3'
    # YELP_SEARCH = 'businesses/search'
    return render(request, 'shops.html', {})
