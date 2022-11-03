from django.contrib import admin
from django.urls import path, re_path, include
from .views import mostar_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mostrar_familiares/', mostar_familiares),
]