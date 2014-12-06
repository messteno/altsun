from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsSerializer
from .models import News
from utils.permissions import IsAdminOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-create_date')
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly, )
    paginate_by = 10
    paginate_by_param = 'count'


class NewsItemViewSet(APIView):
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
