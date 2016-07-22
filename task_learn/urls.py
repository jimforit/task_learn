"""task_learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from taskmanapp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^index/', HostListView.as_view(),name="home_page"),
	url('^showDashboard$',HostListView.as_view(),name="DashBoradPage"),
	url(r'^getCPUInfo/$',getCPUInfo),
	url(r'^getMemInfo/$',getMemInfo),
	url(r'^getDiskInfo/(\w+)$',getDiskInfo),
	url(r'^file_transfer/$',file_transfer),
	url(r'^command_execution$',command_execution),
]
