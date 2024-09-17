#/user_auth/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    # Include Django's built-in authentication views
    path('user_auth/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'),name='home' ),
]