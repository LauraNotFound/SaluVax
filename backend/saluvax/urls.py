"""
URL configuration for saluvax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from vaccinationsys.views import (
    LoteListCreateView, LoteDetailView, 
    RolListCreateView, RolDetailView,
    UsuarioListCreateView, UsuarioDetailView,
    VacunaListCreateView, VacunaDetailView,
    PacienteListCreateView, PacienteDetailView,
    VialListCreateView, VialDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('lotes/', LoteListCreateView.as_view(), name='lote-list-create'),
    path('lotes/<int:pk>/', LoteDetailView.as_view(), name='lote-detail'),
    
    path('roles/', RolListCreateView.as_view(), name='rol-list-create'),
    path('roles/<int:pk>/', RolDetailView.as_view(), name='rol-detail'),

    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),

    path('vacunas/', VacunaListCreateView.as_view(), name='vacuna-list-create'),
    path('vacunas/<int:pk>/', VacunaDetailView.as_view(), name='vacuna-detail'),

    path('pacientes/', PacienteListCreateView.as_view(), name='paciente-list-create'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente-detail'),

    path('viales/', VialListCreateView.as_view(), name='vial-list-create'),
    path('viales/<int:pk>/', VialDetailView.as_view(), name='vial-detail'),

]
