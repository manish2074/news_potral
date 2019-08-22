from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView , DetailView
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

'''class NewsList(ListView):
    model = News   
    context_object_name='news_list'
    template_name='index.html' 
    ordering =['-created_at']'''    

class NewsTemplateView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news= News.objects.all()

        context["latest_news"] =news.order_by("-created_at") [:5]
        context["political_news"] =news.filter(category="0").order_by("-created_at") [:5]
        context["sports_news"] =news.filter(category="1").order_by("-created_at")[:5]
        context["fashion_news"] =news.filter(category="2").order_by("-created_at") [:5]
        context["technology_news"] =news.filter(category="3").order_by("-created_at") [:5]
        return context

class NewsCategoryView(ListView):
    model = News
    ordering = ['-created_at']
    context_object_name = 'category_list'
    template_name="news/category_news.html"

    def get_queryset(self):
        category = self.kwargs.get('category')
        category_key =[item[0] for item in News.CATEGORY if item[1]==category][0]
        return News.objects.filter(category=category_key)

class NewsDetailView(DetailView):
    model = News
    template_name="news/detail_news.html"
        

    
        