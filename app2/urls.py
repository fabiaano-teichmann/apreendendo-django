from django.conf.urls import url
from .import views
urlpatterns = [
url(r'^$',views.index, name = 'index'), 
url(r'^perfil/', views.perfil, name= 'perfil'),
url(r'^post_list/', views.post_list, name= 'blog'),
url(r'^$', views.post_list),
url(r'^blog/(?P<pk>[0-9]+)/$', views.post_detail)
]
#https://docs.djangoproject.com/en/1.9/topics/http/urls/