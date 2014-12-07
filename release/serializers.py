from rest_framework import serializers
from django.db import models
from rest_framework.serializers import Serializer
from embed_video import backends
from .models import Release, Artist, ArtistImage


class ReleaseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    release = serializers.CharField(required=True)
    create_date = serializers.DateTimeField(required=True)

    class Meta:
        model = Release
        fields = ('id', 'name', 'content', 'create_date', 'release', 
                  'embed', 'podcast', )


class ArtistImageSerializer(serializers.ModelSerializer):
    preview_sm = serializers.SerializerMethodField()
    preview_md = serializers.SerializerMethodField()

    class Meta:
        model = ArtistImage
        fields = ('id', 'image', 'preview_sm', 'preview_md', )

    def get_preview_sm(self, obj):
        return obj.preview_sm.url

    def get_preview_md(self, obj):
        return obj.preview_md.url


class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    biography = serializers.CharField(required=True)
    images = ArtistImageSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'biography', 'images', )
