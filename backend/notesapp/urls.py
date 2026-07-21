"""notesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include
import os

def api_running(request):
    server_name = os.getenv("SERVER_NAME", "Unknown Server")
    return HttpResponse(f"API Running properly from {server_name}")

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/running/", api_running),
]