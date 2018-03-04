"""OZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from objectivezero import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
	url(r'^technologies/', views.technologies, name='technologies'),
	url(r'^legalInfo/', views.legalInfo, name='legalInfo'),
    url(r'^signIn/', views.signing, name='signing'),
    url(r'^account/', views.myAccount, name='account'),
	url(r'^trading/', views.trading, name='trading'),
	url(r'^project/', views.project, name='project'),
	url(r'^wastes/', views.wastes, name='wastes'),
]
