from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import News
from .serializers import NewsSerializer


class NewsItemView(APIView):
    model = News

    def get(self, request, pk=None):
        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        serializer = NewsSerializer(news)
        data = serializer.data
        data['neigbours'] = []
        neigbours = news.get_neigbours()
        for neigbour in neigbours:
            serializer = NewsSerializer(neigbour)
            data['neigbours'].append(serializer.data)
        return Response(data)
