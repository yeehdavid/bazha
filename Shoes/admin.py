from django.contrib import admin
from .models import Shoes, Brand

class ShoesAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand',  'price', 'desc']



admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Brand)
# Register your models here.