from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Category

# class PostListView(ListView):
#     model = Post
#     template_name = 'index.html'

def postlist(request):
    posts = Post.objects.order_by('-created_on')
    featured = Post.objects.filter(featured=True)

    if request.method == 'GET' and 'search' in request.GET:
        q = request.GET['search']
        if q is not None and q != '':
            posts = Post.objects.filter(title__contains=q)

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    if featured:
        featured = featured[0]
        return render(request, 'index.html', {'posts': page_posts, 'featured' : featured})

    return render(request, 'index.html', {'posts': page_posts})

class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"

class CategoryListView(ListView):
    template_name = "category.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        posts = Category.objects.get(title=self.category)

        return posts.post_categories.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = str.replace(self.kwargs['slug'], '-', ' ')
        print(self.kwargs['slug'])
        return context

    

