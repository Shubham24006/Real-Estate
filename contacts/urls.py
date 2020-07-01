from django.urls import path

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact'),
  path('enquiry/', views.enquiries, name='enquiry')
  ]

