from django.urls import path
from .views import  postlist

app_name = 'blog'

urlpatterns = [
    path('', postlist, name='index'),
]
