from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='aboutus'),
    path('search', search, name='search'),
    ]

