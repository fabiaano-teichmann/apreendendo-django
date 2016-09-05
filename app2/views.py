from django.shortcuts import  render
#from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Perfil, Post
from .forms import PostForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView
import datetime

def index(request):
	
	posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	
	return render(request, 'app2/index.html', {'posts': posts})

	
	

def perfil(request):
	perfis = Perfil.objects.all()
	
	return render(request, 'app2/perfil.html', {'perfis': perfis})

def listar(request):
	
	posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	
	return render(request, 'app2/listar.html', {'posts': posts})




def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render (request, 'app2/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.publish_date = timezone.now()
			post.save()
			return redirect('app2.view.post_detail', slug=post.slug)
		else:
			form = PostForm()	
		return render(request, 'app2/post_edit.html', {'form': form})


	
