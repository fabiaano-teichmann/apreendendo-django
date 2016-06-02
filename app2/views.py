from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Perfil
import datetime

# Create your views here.
def index(request):
	nome = 'Fabiano Teichamnn'
	data = datetime.datetime.now()
	lista= ['iten1', 'iten2', 'iten2', 'iten4']
	return render(request,'app2/index.html',{'nome':nome, 'data':data, 'lista':lista})
	# estamos retornando/ enviando(return) e entregando /montando (render) para a requisição 
	#foi feita (request) o arquivo 'app2/index.html

def perfil(Perfil):
	nome = perfil.nome
	
	return render(request, 'app2/perfil.html', {'nome': nome})
