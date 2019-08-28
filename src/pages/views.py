from django.core.mail import send_mail
from django.shortcuts import render
from django.http import Http404
from .forms import ContactForm

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

# contact_view()
def contact_view(request):
    form = ContactForm()
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
            form = ContactForm()
    context = {
        "contact_form": form
    }
    return render(request, 'contact.html', context)
