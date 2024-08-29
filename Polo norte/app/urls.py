from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('base', views.base, name='base'),
    path('profile', views.profile, name='profile'),
    path('carrito', views.carrito, name='carrito'),


    # otras URL
]

