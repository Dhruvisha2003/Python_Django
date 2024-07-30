from django.shortcuts import render

# Create your views here.

def home(Request,id):
    list = {"product":[
        {"name" : "FAST Trendy Trainer Execellent Gear Lace-Ups Sporty Running Shoes For Men","price":348,"offers" : "Bank OfferGet ₹50 Instant Discount on first Flipkart UPI transaction on order of ₹200 and above","color":["pink","blue","black"],"size":[6,7,8,9]},
        {"name" : "dfjhkl","price":348,"offers" : "Bank OfferGet ₹50 Instant Discount on first Flipkart UPI transaction on order of ₹200 and above","color":["pink","blue","black"],"size":[6,7,8,9]},
        {"name" : "ghjkm","price":348,"offers" : "Bank OfferGet ₹50 Instant Discount on first Flipkart UPI transaction on order of ₹200 and above","color":["pink","blue","black"],"size":[6,7,8,9]}]}
    x = list["product"][id]
    return render(Request,'home.html',x)
    # return render(Request,"home.html",x)
def index(Request):
    return render(Request, 'index.html')