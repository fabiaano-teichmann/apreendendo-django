from django.conf.urls import url, include , patterns
from .import views
urlpatterns = [
url(r'^$',views.index, name = 'index'), 
url(r'^listar/', views.listar, name= 'listar'),
# url amigável passa expressões - / e letra para a view	
url(r'^blog/(?P<slug>[-\w]+)/$', views.post_detail),
url(r'^post_new/$', views.post_new, name='post_new')
]
#https://docs.djangoproject.com/en/1.9/topics/http/urls/
