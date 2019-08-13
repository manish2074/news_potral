from django.shortcuts import render
from django.views.generic import CreateView
from news import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.urls import reverse_lazy
# Create your views here.

class CreateNewsView(LoginRequiredMixin,CreateView):
    login_url = "/accounts/laogin"
    form_class= forms.CreateNewsForm
    template_name = "news/create_news.html"
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        print("CLEANED_DATA:",form.cleaned_data)
        title = form.cleaned_data['title']
        news= form.save(commit=False)
        news.reporter = self.request.user
        news.slug = slugify(title)
        news.save()
        return super(CreateNewsView, self).form_valid(form)

    def form_invalid(self,form):
        print(form.errors)
        return super (CreateNewsView, self).form_invalid(form)