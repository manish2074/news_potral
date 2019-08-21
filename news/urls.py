from django.urls import path
from news import views
urlpatterns = [
    path('create/', views.CreateNewsView.as_view(),name='create_news'),
    path('<str:category>/', views.NewsCategoryView.as_view(),name='create_news')
]
