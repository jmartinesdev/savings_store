from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Home Page",
        "content": "Home Page"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "About us",
        "content": "About us"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Us",
        "content": "Contact Page",
        "form": contact_form
    }
    if request.method == "POST":
        print(request.POST)
    return render(request, "contact/view.html", context)
    