from django.shortcuts import render
from .models import Menu
from .models import products
from .models import pdetails
from .models import shop
from .models import blogs
from .models import About


# Create your views here.

def index(request):
    menus = Menu.objects.all()
    products_list = products.objects.all()
    product_detail = pdetails.objects.all()
    blog_detail = blogs.objects.all()
    return render(request, 'index.html',{'menus':menus,'products_list':products_list,'product_detail':product_detail,'blog_detail':blog_detail})


def shopPage(request):
    shop_detail = shop.objects.all()
    return render(request,'shop.html',{'shop_detail':shop_detail})

def aboutus(request):
    about_us = About.objects.all()
    return render(request,'about.html',{'about_us':about_us})

def Ourservice(request):
    services = products.objects.all()
    return render(request,'services.html',{'services':services})

def Blog(request):
    blog_list = blogs.objects.all()
    return render(request,'blog.html',{'blog_list':blog_list})

