from django.urls import path
from owners import views

urlpatterns = [
    path('signup',views.SignupView.as_view()),
    path('login',views.LoginView.as_view()),
    path('home',views.HomeView.as_view()),
    path('products/add',views.AddproductView.as_view())
]