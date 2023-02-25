from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.ManyToManyField(Category, blank=True, related_name='post_categories')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=False)
        super().save(*args, **kwargs)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True, related_name='replies')
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'