from django.urls import path
from news import views
urlpatterns = [
    path('create/', views.CreateNewsView.as_view(),name='create_news'),
    path('<str:category>', views.NewsCategoryView.as_view(),name='category_news'),
    path('<str:category>/<int:pk>/<str:slug>/', views.NewsDetailView.as_view(),name='detail_news')
]
