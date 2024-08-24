from django.shortcuts import render
from .models import Menu
from .models import products
from .models import pdetails
from .models import shop

# Create your views here.

def index(request):
    menus = Menu.objects.all()
    products_list = products.objects.all()
    product_detail = pdetails.objects.all()
    shop_detail = shop.objects.all()
    return render(request, 'index.html',{'menus':menus,'products_list':products_list,'product_detail':product_detail,'shop_detail':shop_detail})
