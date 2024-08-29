from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'app/base.html', {
    })
def home(request):
    return render(request, 'app/home.html', {
    })
def profile(request):
    return render(request, 'app/profile.html', {
    })


def login(request):
    return render(request, 'app/login.html', {
    })
def registro(request):
    return render(request, 'app/registro.html', {
    })


def carrito(request):
    return render(request, 'app/carrito.html', {
    })
