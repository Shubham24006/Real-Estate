from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('dashboard/<int:pk>', login_required(Dashboard.as_view()), name='dashboard'),
    path('update/<int:pk>', login_required(ProfileUpdate.as_view()), name='profileupdate'),
    path('password/', change_password, name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
         template_name='accounts/password_reset.html', email_template_name='accounts/password_reset_email.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
         template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
         template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
         template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]