from django.contrib import admin
from .models import Property

# Register your models here.


class PropertyAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    list_display = ('name', 'city', 'state', 'price', 'photo_main',)
    list_filter = ('name', 'city', 'state', 'price')


admin.site.register(Property, PropertyAdmin)
