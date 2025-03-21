from django.contrib import admin

# Register your models here.
from django.apps import AppConfig

from .models import alumne
from .models import professor

@admin.register(alumne)
class alumnes(admin.ModelAdmin):
    pass
#    list_display = ('name', 'surname', 'email', 'edat' ,'genere','curs','moduls','tutor','id')


@admin.register(professor)
class professors(admin.ModelAdmin):
    pass