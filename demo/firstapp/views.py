from django.shortcuts import render

# Create your views here.

def home(Request):
    return render(Request, 'home.html')

def index(Request):
    return render(Request, 'index.html')