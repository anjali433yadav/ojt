
from django.shortcuts import render
from .models import HomePage, ServicesPage, ContactPage

def home(request):
    page = HomePage.objects.first()
    return render(request, "home.html", {"page": page})


def services(request):
    page = ServicesPage.objects.first()
    return render(request, "services.html", {"page": page})


def contact(request):
    page = ContactPage.objects.first()
    return render(request, "contact.html", {"page": page})

