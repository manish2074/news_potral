from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, ListView,TemplateView , DetailView , UpdateView , DeleteView
from news import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.text import slugify
from news.models import News, Comment
# Create your views here.

class CreateNewsView(LoginRequiredMixin,CreateView):
    login_url = "/account/login"
    form_class = forms.CreateNewsForm
    template_name = "news/create_news.html"
    success_url = reverse_lazy('home')


    def form_valid(self,form):
        
        news = form.save(commit=False)
        title= form.cleaned_data['title']
        news.reporter = self.request.user
        news.slug = slugify(title)
        news.save()
        return super(CreateNewsView,self).form_valid(form)


    def form_invalid(self,form):
        print (form.errors)
        return super(CreateNewsView,self).form_invalid(form)  
   

'''class NewsList(ListView):
    model = News
    context_object_name='news_list'
    template_name='index.html'
    ordering=['-created_at']'''   

class NewsTemplateView(TemplateView):
    template_name="index.html"
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news=News.objects.all()
    
        context["latest_news"] = news.order_by("-created_at") [:5]
        context["political_news"] = news.filter(category="0").order_by("-created_at") [:5]
        context["sports_news"] = news.filter(category="3").order_by("-created_at") [:5]
        context["fashion_news"] = news.filter(category="1").order_by("-created_at") [:5]
        context["business_news"] = news.filter(category="2").order_by("-created_at") [:5]
        context["popular_news"] = news.order_by("-count")[:5]
        
        return context

    

class NewsCategoryView(ListView):
    model = News
    ordering =['-created_at']
    context_object_name ='category_list'
    template_name="news/category_news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.kwargs.get('category')
        return context

    def get_queryset(self):
        category = self.kwargs.get("category")
        category_key = [item[0] for item in News.CATEGORY if item[1] == category][0]
        return News.objects.filter(category=category_key)
            
class NewsDetailView(DetailView):
    model = News
    template_name='news/detail_news.html'
    context_object_name= 'news'
   
   
    def get_context_data(self, **kwargs):
        news=News.objects.all()
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(news=self.object)
        context["popular_news"] = news.order_by("-count")[:5]
        self.object.count = self.object.count + 1
        self.object.save()
        return context

  
    

class NewsUpdateView(LoginRequiredMixin,UpdateView):
    model = News
    template_name="news/update_news.html"
    fields = ("title","story")
    success_url=reverse_lazy("home")

class NewsDeleteView(LoginRequiredMixin,DeleteView):
    model = News
    
    success_url=reverse_lazy("home")
@login_required
def create_comment(request,**kwargs):
    data=request.POST
    news = get_object_or_404(News,pk=kwargs.get('pk'))
    feedback = data.get('feedback')
    comment_by = request.user
    payload = {"news":news,"comment_by":comment_by,"feedback":feedback}
    comment = Comment(**payload)
    comment.save()
    return render(request,"news/comment.html",{"comment":comment})

def news_single(request,slug):
    news = get_object_or_404(Comment, slug=slug)
    news_related = news.tags.similar_objects()
    return render(request,'detail_news.html',
    {'news':news ,'news_related':news_related})    
   
