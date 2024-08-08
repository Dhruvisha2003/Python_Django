from django.shortcuts import *
from App.models import User
from App.models import register
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        user = User(name=name,email=email,password=password)
        user.save()
    return render(request, 'home.html')

def show(request):
    data  = User.objects.all()
    # print(data)
    return render(request, 'show.html',{'data':data})

def showone(request,id):
    data = User.objects.get(id=id)
    return render(request, 'show.html',{'data':[data]})

def deldata(request,id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('show')

def update(request,id):
    data = User.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        data.name = name
        data.email = email
        data.password = password
        data.save()
        return redirect('show')
    return render(request,"update.html",{"data":data}) 

# def login(request):
#     return render(request,'login.html')


#make registration form with name gender email password and insert value to database
#make login form with email password
#make show all users form
#make show one user form
#make delete user form
#make update user form

def insert1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        reg = register(name=name,gender=gender,email=email,password=password)
        reg.save()
        return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = register.objects.filter(email=email,password=password)
        if user:
            return HttpResponse("Hello!!")
        else:
            return HttpResponse("Invalid Email or Password")
