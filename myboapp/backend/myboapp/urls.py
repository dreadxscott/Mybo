"""
URL configuration for myboapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import get_csrf_token_view


urlpatterns = [
    #urls for japanese learner
    path('japanese_learner/', include('japanese_learner.urls')),

    #urls for chatbot

    #urls for authentication
    path('', include('user_auth.urls')),

    #urls for accounts
    path("accounts/", include("accounts.urls")),  # new

    #main urls
    path('admin/', admin.site.urls),

    #jwt urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #csrf vurls
    path('api/csrf/', get_csrf_token_view, name='get_csrf_token_view')
]


