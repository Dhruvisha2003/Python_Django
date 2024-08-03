from django.shortcuts import render
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