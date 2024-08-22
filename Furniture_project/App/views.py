from django.shortcuts import render
from .models import menu
from .models import products

def index(request):
    menus = menu.objects.all()
    products_list = products.objects.all()
    return render(request, 'index.html',{'menus':menus,'products_list':products_list})

