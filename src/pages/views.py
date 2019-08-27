from django.shortcuts import render
from django.http import Http404

# Create your views here.

# home_view()
def home_view(request):
    try:
        return render(request, 'home.html')
    except:
        raise Http404('Page does not exist')

# about_view()
def about_view(request):
    try:
        return render(request, 'about.html')
    except:
        raise Http404('Page does not exist')

def contact_view(request):
    try:
        return render(request, 'contact.html')
    except:
        raise Http404('Page does not exist')
