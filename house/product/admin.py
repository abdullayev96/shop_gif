from django.contrib import admin
from .models import *

class  AdminCustomer(admin.ModelAdmin):
    list_display = ('id', 'title',  'price', 'photo', 'create_at')
    list_display_links = ("id", "title")
    search_fields = ("id", "title", 'price')

admin.site.register(Customer, AdminCustomer)
admin.site.register(Category)



