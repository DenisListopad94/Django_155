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

class ManufactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'city', 'worker')
    list_display_links = ('id', 'country')
    search_fields = ('country', 'city')

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'finance', 'detail')
    list_display_links = ('name', 'detail')
    search_fields = ('name', 'detail')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age','email')
    list_display_links = ('name', 'email')
    search_fields = ('surname', 'email')

admin.site.register(Car,CarsAdmin)
admin.site.register(Manufacture,ManufactureAdmin)
admin.site.register(Provider,ProviderAdmin)
admin.site.register(Director,DirectorAdmin)
