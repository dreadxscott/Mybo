from django.forms.models import BaseModelForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .form.forms import CustomUserCreationForm  # Your custom form for user registration
from .models import CustomUser


class CustomUserRegistrationView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm

    def form_valid(self, form):
            form.save()  # Save the new user to the database
            # Return a JSON response instead of redirecting to a new page
            return JsonResponse({'message': 'User created successfully'}, status=201)

    def form_invalid(self, form):
        # Return validation errors in a JSON format
        return JsonResponse({'errors': form.errors}, status=400)