from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def addcart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def services(request):
    return render(request, 'services.html')

def shop(request):
    return render(request, 'shop.html')

def thanks(request):
    return render(request, 'thankyou.html')

def contact(request):
    return render(request, 'contact.html')