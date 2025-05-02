from django.contrib import admin
from django.apps import AppConfig
from .models import User

@admin.register(User)
class User(admin.ModelAdmin):
    pass
