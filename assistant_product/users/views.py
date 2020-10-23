from django.views.generic import CreateView
from .forms import CreationForm
from django.urls import reverse_lazy
from django.shortcuts import render


class SignUp(CreateView):
    form_class = CreationForm
    success_url = "/auth/login/"
    template_name = "signup.html"
