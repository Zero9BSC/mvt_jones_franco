from django.contrib import admin
from django.urls import path, re_path, include
from mvt_jones_franco import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('Familiares.url'))
]
