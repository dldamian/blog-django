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

    if request.method == 'GET' and 'search' in request.GET:
        q = request.GET['search']
        if q is not None and q != '':
            posts = Post.objects.filter(title__contains=q)

    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    

    return render(request, 'index.html', {'posts': page_posts})