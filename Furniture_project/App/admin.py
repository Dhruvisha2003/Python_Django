from django.contrib import admin
from .models import menu
from .models import products

admin.site.register(menu)
admin.site.register(products)