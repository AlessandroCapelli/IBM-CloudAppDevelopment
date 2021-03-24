from django.contrib import admin
from .models import CarMake, CarModel 


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name']

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['carmake']

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)