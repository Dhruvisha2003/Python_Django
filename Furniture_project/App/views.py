from django.shortcuts import render
from .models import menu
from .models import products

def index(request):
    all=menu.objects.all()
    product = products.objects.all()
    return render(request, 'index.html',{'all':all,'product':product})

