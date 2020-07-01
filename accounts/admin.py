from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_seller' )

admin.site.register(Profile, ProfileAdmin)
