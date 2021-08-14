from django.shortcuts import render

def register_form(request, city_name):
    return render(request, 'register_form.html')

def index(request):
    return render(request, 'index.html')