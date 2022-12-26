from django.contrib import admin

from home.models import UserProfile,Products
from home.models import Setting ,ContactFormMessage

# Register your models here.ü

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject',]

admin.site.register(UserProfile)
admin.site.register(Products)
admin.site.register(Setting)
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)