from django.shortcuts import render

def register_form(request, city_name):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')