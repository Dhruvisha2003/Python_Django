from django.shortcuts import render
from django.http import HttpResponse
from app1.models import User
# Create your views here.
def home(request):
    return render(request,'home.html')
    # return HttpResponse("done")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def header(request):
    return render(request, 'header.html')
def footer(request):
    return render(request, 'footer.html')

def formget(request):
    name=""
    email=""
    password=""
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        password = request.GET.get('password')
        
    return render(request,"form.html",{"name":name,"email":email,"password":password})

def formpost(request):
    name=""
    email=""
    password=""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

    return render(request,"form.html",{"name":name,"email":email,"password":password})