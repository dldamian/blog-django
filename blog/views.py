from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Post

# class PostListView(ListView):
#     model = Post
#     template_name = 'index.html'

def postlist(request):
    posts = Post.objects.order_by('-created_on')
    paginator = Paginator(posts, 5)
    context = {'posts': posts,}

    return render(request, template_name='index.html', context=context)