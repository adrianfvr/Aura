from django.urls import path
from .views import registro, cerrar_sesion
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]