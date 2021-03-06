from django.contrib import admin
from .models import Perfil, Post, Img
class PerfilAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('nome', 'sobre_nome','genero', 'favorito')
	list_filter=('genero', 'favorito')

class Meta:
	model = Perfil
	admin.site.register(Perfil, PerfilAdmin)	
# Post

class PostAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('author', 'title', 'publish_date')
	list_filter = ('author', 'title') 
	prepopulated_fields = {'slug': ("title",)} # preencher automáticamente slug baseado no título
class MetaPost:
	model = Post
	admin.site.register(Post, PostAdmin)

class ImgAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display =('title', 'id_img')	
class MetaImg:
	model = Img
	admin.site.register(Img, ImgAdmin)