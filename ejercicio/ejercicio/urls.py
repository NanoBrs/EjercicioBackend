"""
URL configuration for ejercicio project.

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
from ejercicioApp.views import renderHome,renderJuguetes,renderRopa,renderElectronica

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', renderHome),
    path('juguetes/',renderJuguetes),
    path('ropa/',renderRopa),
    path('electronica/',renderElectronica)
]
