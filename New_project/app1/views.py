from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def send(request,id):
    li = ["produc1","product2","product3"]
    return HttpResponse(li[id])
    # print("hello world")

def product(request,id):
    products = ["Watch","Rings","Necklace","Bracelet","Gold Coins","Earrings","Chain","Nose pins","Anklets"]
    return HttpResponse(products[id]) 

def call(request):
    return render(request,"index.html")