"""
proyecto/urls.py
Archivo de rutas principal del proyecto.
Incluye rutas del admin y delega las rutas principales a la app dashboard.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),  # Envia las rutas raíz a dashboard
]


