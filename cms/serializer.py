# coding: utf-8

from rest_framework import serializers

from .models import Product, Article, BlogPost
from .service import get_html_from_text


class CustomSerializer(serializers.HyperlinkedModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(
            CustomSerializer,
            self).get_field_names(
            declared_fields,
            info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class ProductSerializer(CustomSerializer):
    #id = serializers.Field()
    class Meta:
        model = Product
        fields = "__all__"
        extra_fields = ["id"]


class ArticleSerializer(CustomSerializer):
    # html source parsed from "detail" (markdown format)
    parsed_detail: str = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"
        extra_fields = ["id", "parsed_detail"]

    def get_parsed_detail(self, obj: Article) -> str:
        """get parsed detail

        Args:
            value (str): markdown format

        Returns:
            str: html parsed from detail
        """
        return get_html_from_text(obj.detail)


class BlogPostSerializer(CustomSerializer):
    # html source parsed from "detail" (markdown format)
    parsed_detail: str = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = "__all__"
        extra_fields = ["id", "parsed_detail"]

    def get_parsed_detail(self, obj: BlogPost) -> str:
        """get parsed detail

        Args:
            value (str): markdown format

        Returns:
            str: html parsed from detail
        """
        return get_html_from_text(obj.detail)
