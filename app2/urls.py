from django.conf.urls import url
from .import views
urlpatterns = [
url(r'^$',views.index, name = 'index'), 
url(r'^perfil/', views.perfil, name= 'perfil'),
url(r'^post_list/', views.post_list, name= 'blog'),
]