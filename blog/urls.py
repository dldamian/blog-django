from django.urls import path
from .views import  postlist

urlpatterns = [
    path('', postlist),
]
