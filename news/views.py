from django.shortcuts import render
from django.views.generic import CreateView
from news import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class CreateNewsView(LoginRequiredMixin,CreateView):
    login_url = "/accounts/login"
    form_class= forms.CreateNewsForm
    template_name = "news/create_news.html"