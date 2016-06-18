from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Perfil, Post
import datetime

# Create your views here.
def index(request):
	nome = 'Fabiano Teichamnn'
	data = datetime.datetime.now()
	lista= ['iten1', 'iten2', 'iten2', 'iten4']
	return render(request,'app2/index.html',{'nome':nome, 'data':data, 'lista':lista})
	# estamos retornando/ enviando(return) e entregando /montando (render) para a requisição 
	#foi feita (request) o arquivo 'app2/index.html

def perfil(request):
	perfis = Perfil.objects.all()
	
	return render(request, 'app2/perfil.html', {'perfis': perfis})

def post_list(request):
	
	posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	
	return render(request, 'app2/post_list.html', {'posts': posts})
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render (request, 'app2/post_detail.html', {'post': post})

	