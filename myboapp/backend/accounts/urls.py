from django.urls import path

from user_auth.views import CustomUserRegistrationView


urlpatterns = [
    path("signup/", CustomUserRegistrationView.as_view(), name="signup"),
]