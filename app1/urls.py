# -*- coding: utf-8 -*-
from django.conf.urls import url
from .import views
urlpatterns = [
url(r'^ola/mundo/$', views.ola_mundo, name= 'ola_mundo'),
url(r'^soma/$', views.soma, name = 'soma'),
url(r'^data/$', views.data_hora, name ='data_hora'),
url(r'^status/$', views.status_code, name= 'status_code'),	

]
