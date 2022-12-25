from django.contrib import admin

from home.models import UserProfile,Products
from home.models import Setting

# Register your models here.ü



admin.site.register(UserProfile)
admin.site.register(Products)
admin.site.register(Setting)