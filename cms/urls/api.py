from rest_framework import routers
import os
import sys

try:
    from cms.views import ProductViewSet, ArticleViewSet, BlogPostViewSet
except BaseException:
    raise


router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'blog_posts', BlogPostViewSet)

urlpatterns = router.urls
