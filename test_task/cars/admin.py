from django.contrib import admin

from .models import *

class CarAdmin(admin.ModelAdmin):
    # list_display = ["name","email"]
    list_display = [field.name for field in Car._meta.fields]
    search_fields = ['title']
    class Meta:
        model = Car

admin.site.register(Category)
admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)

