"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url

from my_app import views
from my_app.views import HomeView,FormView,Main_page,Ip_to_Dom

app_name = 'my_app'
urlpatterns = [
    url(r'^$' , Main_page.as_view() , name = 'Home'),
    path('formm/', FormView.as_view(), name='formm'),
    path('index/', HomeView.as_view(), name='index'),
    #path('Home/', Main_page.as_view(), name='Home'),
    path('ip_to_dom/', Ip_to_Dom.as_view(), name='ip_to_dom'),

    #url(r'^$' , views.domain_name , name = 'domain_name'),
]
