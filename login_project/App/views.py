from django.shortcuts import *
from App.models import User
from django.views.decorators.cache import cache_control
from django.contrib import messages

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signin(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            data = User.objects.get(email=email,password=password)
            print("Session_id =",data.id)
            request.session['id'] = data.id
            print('session set')
            return redirect('home') 
        except:
            messages.error(request, 'User not found in the Register table!!! Please Register ')
            return redirect('login')
    else:
        return render(request,'login.html')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)   
def logout(request):
    if 'id' in request.session:
        del request.session['id']
        print('Deleted session ID')
      
    
    return redirect("/")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    data1 = request.session.get('id')
    if data1:
        print("=-------------------==-=-=-=-=-=-=-")
        return render(request,'home.html',{'data1':data1})
    else:
        return redirect('login')