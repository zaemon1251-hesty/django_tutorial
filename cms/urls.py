# coding: utf-8

from rest_framework import routers
from .views import ProductViewSet, ArticleViewSet, BlogPostViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'blog_posts', BlogPostViewSet)

urlpatterns = router.urls