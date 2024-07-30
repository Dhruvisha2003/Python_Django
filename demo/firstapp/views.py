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

def index(Request,id):
    products = {"product" :[
        {"name":"Lip Mousse","price":"₹629","shades":["Pink","Brown","Red","Orange"],"offer":"30% OFF"},
        {"name":"Skin Tint Foundation","price":"₹719","shades":["Sand","Lisa","Norma","Margot"],"offer":"20% OFF"},
        {"name":"Blush ","price":"₹509","shades":["Pink","Brown","Red","Coral"],"offer":"15% OFF"},
        {"name":"Lip Mousse - 304 Chocolate Temptation","price":"₹629","shades":["Pink","Brown","Red","Orange"],"offer":"30% OFF"},
        {"name":"Nail Lacquer","price":"₹99","shades":["Pink","Brown","Red","Orange"],"offer":"10% OFF"},
        {"name":"Mascara","price":"₹629","shades":["Black","Brown","Blue","Clear"],"offer":"5% OFF"},
        {"name":"Concealer","price":"₹540","shades":["Green","Orange","Peach","Purple"],"offer":"5% OFF"}
    ]}
    x = products["product"][id]
    return render(Request, 'index.html',x)
