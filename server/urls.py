"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import django
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from server.views import *
from .views import signup_view, user_login, logout_user

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', startPage, name='start'),
    path('signup/', signup_view, name="signup"),
    path('login/', user_login, name="login"),
    path('logout/',logout_user, name='logout'),
    path('cabinet/',include('web.urls')),
)
