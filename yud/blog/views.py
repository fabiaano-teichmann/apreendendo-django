from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def listar(request):
	texto = 'Olá Mundo'
	return HttpResponse(texto)