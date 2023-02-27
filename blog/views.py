from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'index.html'

def postlist(request):
    pass