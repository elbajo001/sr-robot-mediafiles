from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'document', 'first_name', 'last_name', 'genre', 'phone_num', 'phone_num_wa', 'email_address', 'home_address', 'office_address', 'created_at', 'updated_at']

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'description', 'media']