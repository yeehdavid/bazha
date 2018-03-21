from django.contrib import admin
from .models import  Buyer_category, Buyer

class BuyerAdmin(admin.ModelAdmin):
    list_display = ['name','shoes', 'tel', 'address', 'wechat', 'category', 'created_time']

admin.site.register(Buyer_category)
admin.site.register(Buyer, BuyerAdmin)
# Register your models here.
