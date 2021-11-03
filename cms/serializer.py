# coding: utf-8

from rest_framework import serializers

from .models import Product, Article, BlogPost


class CustomSerializer(serializers.HyperlinkedModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

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
    #id = serializers.Field()
    class Meta:
        model = Article
        fields = "__all__"
        extra_fields = ["id"]


class BlogPostSerializer(CustomSerializer):
    #id = serializers.Field()
    class Meta:
        model = BlogPost
        fields = "__all__"
        extra_fields = ["id"]
