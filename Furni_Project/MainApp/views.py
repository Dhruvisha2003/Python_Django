from django.shortcuts import *
from django.http import HttpResponse
from .models import Menu
from .models import products
from .models import pdetails
from .models import shop
from .models import blogs
from .models import About
from .models import blog_list
from .models import register


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
    blog_detail = blog_list.objects.all()
    return render(request,'blog.html',{'blog_detail':blog_detail})

def contact(request):
    return render(request,'contact.html')

def addcart(request):
    return render(request,'cart.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = register(username=username,email=email,password=password,cpassword=cpassword)
        user.save()
        return redirect('login')
    return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        log = register.objects.filter(email=email,password=password)
        if log:
            return redirect('/')
        else:
            return HttpResponse('Invalid Email or Password')