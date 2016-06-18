from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
escolha_sexo = (
	('MASCULINO', 'Masculino'),
	('FEMININO', 'Feminino'),
	)
class Perfil(models.Model):
	nome = models.CharField('Nome:', max_length=10)
	sobre_nome = models.CharField('Sobre nome:', max_length=20)
	genero = models.CharField('Sexo:', max_length=10, choices= escolha_sexo)
	facebook = models.URLField('Facebook:')
	email = models.EmailField('Digite seu E-mail:')
	favorito = models.BooleanField('Favorito:')
	def __str__(self):
		return self.nome
class Post(models.Model):
    author = models.ForeignKey ('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug / URL", help_text="Preenchido automaticamente, não editar.",)
    def publish(self):
    	self.publish_date = timezone.now()
    	self.save()
    def __str__(self):
    	return self.title
    	




