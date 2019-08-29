from django.core.mail import send_mail
from django.shortcuts import render
from django.http import Http404
from .forms import ContactForm

'''
home_view()

Renders the home page [home.html]

Args:
    request: Determines if home_view is being requested

Returns:
    render: Loads the home page when GET request is recieved

Raise:
    Http404: Just for anything that goes wrong
'''

def home_view(request):
    try:
        return render(request, 'home.html')
    except:
        raise Http404('Page does not exist')

'''
about_view()

Renders the about page [about.html]

Args:
    request: Determines if about_view is being requested

Returns:
    render: Loads the about page when GET request is recieved

Raise:
    Http404: Just for anything that goes wrong
'''

def about_view(request):
    try:
        return render(request, 'about.html')
    except:
        raise Http404('Page does not exist')

'''
contact_view()

Uses ContactForm() in forms.py to get valid data from user via a POST
request. If valid, send message to me via email.

https://docs.djangoproject.com/en/dev/topics/email/

Args:
    request: Determines if contact_view is being requested

Returns:
    render: Loads the contact page when a GET/POST request is recieved

Raise:
    Http404: Just for anything that goes wrong
'''

def contact_view(request):
    try:
        form = ContactForm()
        success = False
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                message = '{}\n\n{}'.format(form.cleaned_data['message'], name)
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['evangelistagico@gmail.com'],
                    fail_silently=False
                )
                success = True
                form = ContactForm()
        context = {
            "contact_form": form,
            "success": success
        }
        return render(request, 'contact.html', context)
    except:
        raise Http404('Page does not exist')
