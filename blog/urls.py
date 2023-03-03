from django.urls import path
from .views import  postlist, PostDetailView, CategoryListView

app_name = 'blog'

urlpatterns = [
    path('', postlist, name='index'),
    path('<slug:slug>', PostDetailView.as_view(), name='post'),
    path('category/<slug:slug>', CategoryListView.as_view(), name='category'),
]
