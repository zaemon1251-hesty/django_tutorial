from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, filters
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseNotAllowed, QueryDict
from json import dumps

from .service import get_html_from_text
from .models import Product, Article, BlogPost
from .serializer import ProductSerializer, ArticleSerializer, BlogPostSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer


def render_markdown(request: HttpRequest):
    # only allow POST & ajax
    if request.method == "POST" and request.is_ajax():
        dic = QueryDict(request.body, encoding='utf-8')
        text: str = dic.get('detail')
        return HttpResponse(dumps({
            'detail': get_html_from_text(text)
        }), content_type='application/json')
    return HttpResponseNotAllowed(['POST'])


def check(request: HttpRequest):
    return HttpResponse('this is cms')
