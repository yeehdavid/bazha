from django.contrib import admin
from .models import  Article, Article_Part

class A_Admin(admin.ModelAdmin):
    list_display = ['title', 'created_time']
class A_P_Admin(admin.ModelAdmin):
    list_display = ['belong_to','text','img']

admin.site.register(Article,A_Admin,)
admin.site.register(Article_Part,A_P_Admin)

# Register your models here.
