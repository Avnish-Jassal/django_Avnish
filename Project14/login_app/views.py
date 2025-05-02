from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.shortcuts import render, redirect
from .forms import CrearCuenta

from .forms import CrearCuenta

def CrearCuenta_view(request):
    if request.method == 'POST':
        form = CrearCuenta(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = CrearCuenta()
    return render(request, 'CrearCuenta.html', {'form': form})

def index(request):
    error = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = "Password or username doesn't match"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error': error})

@login_required(login_url='/')
def home_view(request):
    return render(request, 'home.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')
