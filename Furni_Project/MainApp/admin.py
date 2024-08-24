from django.contrib import admin
from .models import Menu
from .models import products
from .models import pdetails
from .models import shop

admin.site.register(Menu)
admin.site.register(products)
admin.site.register(pdetails)
admin.site.register(shop)
