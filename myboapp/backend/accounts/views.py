from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@ensure_csrf_cookie
def get_csrf_token_view(request):
    return JsonResponse({'detail': 'CSRF cookie set!'})