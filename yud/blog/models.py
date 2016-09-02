from django.db import models
from django.utils import timezone

class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField('None:',max_length=80)
	sub_titulo = models.CharField('Sub titulo', max_length= 150)
	texto = models.TextField()
	postado = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.titulo
