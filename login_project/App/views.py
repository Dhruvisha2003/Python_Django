from django.shortcuts import *
from App.models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']
        reg = User(name=name,contact=contact,gender=gender,email=email,password=password)
        reg.save()
        return redirect('login')
    return render(request,'register.html')
        
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = User.objects.filter(email=email,password=password)
        if data:
            return render(request,'home.html')
        else:
            return HttpResponse("Invalid Email or Password")
    else:
        return render(request,'login.html')
