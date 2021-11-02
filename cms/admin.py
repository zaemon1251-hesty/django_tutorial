from django.contrib import admin
from cms.models import Product, Article, BlogPost

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)  # 一覧に出したい項目
    list_display_links = ('id', 'title',)  # 修正リンクでクリックできる項目
admin.site.register(Product, ProductAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)  # 一覧に出したい項目
    list_display_links = ('id', 'title',)  # 修正リンクでクリックできる項目
admin.site.register(Article, ArticleAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)  # 一覧に出したい項目
    list_display_links = ('id', 'title',)  # 修正リンクでクリックできる項目
admin.site.register(BlogPost, BlogPostAdmin)