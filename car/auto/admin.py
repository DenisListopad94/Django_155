from django.contrib import admin
from .models import *



class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'costs', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('costs',)
    list_filter = ('title','costs','description')
    list_per_page = 3 # пагинация
    ordering = ('title','costs')

admin.site.register(Car,CarsAdmin)