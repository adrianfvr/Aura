from django.urls import path
from .views import registro, cerrar_sesion
from .views_auth import login_view

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]
