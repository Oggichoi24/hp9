from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path('add/', views.add_laptop, name="laptop"),
    path("cart/", views.get_cart, name="cart"),


]  