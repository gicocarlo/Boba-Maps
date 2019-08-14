from django.shortcuts import render

# Create your views here.

# home_view()
def home_view(request):
    return render(request, 'html/home.html')

# about_view()
def about_view(request):
    pass
