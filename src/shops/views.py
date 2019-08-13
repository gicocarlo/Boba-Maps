from django.shortcuts import render

# Create your views here.
def shops_view(request):
    return render(request, 'shops.html', {})
