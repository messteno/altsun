from rest_framework import serializers
from news.models import News, NewsImage
from django.db import models
from rest_framework.serializers import Serializer


class NewsImageSerializer(serializers.ModelSerializer):
    preview_sm = serializers.SerializerMethodField()
    preview_md = serializers.SerializerMethodField()

    class Meta:
        model = NewsImage
        fields = ('id', 'image', 'preview_sm', 'preview_md', )

    def get_preview_sm(self, obj):
        return obj.preview_sm.url

    def get_preview_md(self, obj):
        return obj.preview_md.url


class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    create_date = serializers.DateTimeField(required=True)
    images = NewsImageSerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'create_date', 'images', )
