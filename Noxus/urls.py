"""
URL configuration for Noxus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noxus/', include('noxusapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

handler404 = "noxusapp.views.handle404error"
handler400 = "noxusapp.views.handle404error"
handler403 = "noxusapp.views.handle404error"
#handler500 = "noxusapp.views.handle404error"