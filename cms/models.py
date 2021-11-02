from django.db import models

# Create your models here.

class Product(models.Model):
    """成果物"""
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=2000)
    href = models.CharField(blank=True, max_length=2000)
    eyecatch = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    """記事"""
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=2000)
    detail = models.TextField(blank=True)
    href = models.CharField(blank=True, max_length=2000)
    eyecatch = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """ブログ"""
    title = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=2000)
    eyecatch = models.ImageField(blank=True)
    detail = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
