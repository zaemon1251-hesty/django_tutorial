from django.db import models
from django.db.models.signals import post_delete, post_save
import urllib.request
import os
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


def after_crud(sender, instance, *args, **kwargs):
    urllib.request.Request(os.getenv("DEPLY_HOOK_URL"), method='POST')
    print(sender)


for model in [Product, Article, BlogPost]:
    post_save.connect(after_crud, sender=model)
    post_delete.connect(after_crud, sender=model)
