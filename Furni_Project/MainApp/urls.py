"""
URL configuration for Furni_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('shop/',views.shopPage,name='shop'),
    path('about/',views.aboutus,name='aboutus'),
    path('services/',views.Ourservice,name='services'),
    path('blog/',views.Blog,name='Ourblog'),
    path('contact/',views.contact,name='contactUs'),
    path('Cart/',views.addcart,name='addcart')
]
