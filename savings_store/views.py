from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

@login_required
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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print("Login Valid")
            login(request, user)
            return redirect("/")
        else: 
            print("Invalid Login")

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)
        
    