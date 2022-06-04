from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import userLoginForm, userRegisterForm
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Bienvenue a tous</h1>")
    return render(request, "general/home.html")

def userLoginView(request):
    next = request.GET.get('next')
    form = userLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    # Avec ca je peux afficher des champs de tables diffrentes
    context = {
        'form': form,
    }
    return render(request, "login.html", context)
