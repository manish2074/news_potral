from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from account import views
urlpatterns =[
    path('login/', LoginView.as_view(template_name="account/login.html"), name='login' ),
    path('logout/', LogoutView.as_view(template_name="index.html"), name='logout'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
]