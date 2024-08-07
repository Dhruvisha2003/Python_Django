from django.shortcuts import *
from App.models import User
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

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(fname=fname,lname=lname,gender=gender,email=email,password=password)
        user.save()
    return render(request,'register.html')