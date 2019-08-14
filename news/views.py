from django.shortcuts import render
from django.views.generic import CreateView, ListView
from news import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.urls import reverse_lazy
from news.models import News
# Create your views here.

class CreateNewsView(LoginRequiredMixin,CreateView):
    login_url = "/accounts/login"
    form_class= forms.CreateNewsForm
    template_name = "news/create_news.html"
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        title = form.cleaned_data['title']
        news= form.save(commit=False)
        news.reporter = self.request.user
        news.slug = slugify(title)
        news.save()
        return super(CreateNewsView, self).form_valid(form)

    def form_invalid(self,form):
        print(form.errors)
        return super (CreateNewsView, self).form_invalid(form)

class NewsList(ListView):
    model = News   
    context_object_name='news_list'
    template_name='index.html' 
    ordering =['-created_at']    