import django_filters
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, filters
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseNotAllowed
from .service import get_html_from_text
from .models import Product, Article, BlogPost
from .serializer import ProductSerializer, ArticleSerializer, BlogPostSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


def render_markdown(request: HttpRequest):
    # only allow POST ajax
    if request.method == 'POST' and request.is_ajax():
        text: str = request.POST.get('detail')
        return JsonResponse({
            'detail': get_html_from_text(text)
        })
    return HttpResponseNotAllowed(['POST'])


def check(request: HttpRequest):
    return HttpResponse('this is cms')
