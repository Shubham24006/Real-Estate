from django.urls import path
from .views import listings, listing, SaveProperty, PropertyUpdate, DeleteProperty, listing_slug
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listings/', listings, name='listings'),
    # path('listing/<int:id>/', listing, name='property'),
    path('listing/<slug:property>/', listing_slug, name='property'),
    path('postproperty/', login_required(SaveProperty.as_view()), name='postproperty'),
    path('updateproperty/<int:pk>', login_required(PropertyUpdate.as_view()), name='updateproperty'),
    path('deleteproperty/<int:pk>', login_required(DeleteProperty.as_view()), name='deleteproperty'),
    ]

