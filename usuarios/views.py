from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')