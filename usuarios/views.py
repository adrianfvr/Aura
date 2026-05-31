from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm


def registro(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido a AURA, {user.username}! Tu cuenta ha sido creada.')
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})


def cerrar_sesion(request):
    username = request.user.username
    logout(request)
    messages.info(request, f'Hasta luego, {username}.')
    return redirect('/')
