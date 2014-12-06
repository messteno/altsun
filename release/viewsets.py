from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from utils.permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReleaseSerializer, ArtistSerializer
from .models import Release, Artist


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all().order_by('-create_date')
    serializer_class = ReleaseSerializer
    permission_classes = (IsAdminOrReadOnly, )
    paginate_by = 6
    paginate_by_param = 'count'
    filter_fields = ('podcast', )


class ReleaseItemViewSet(APIView):
    model = Release

    def get(self, request, pk=None):
        podcast = request.GET.get('podcast')
        if podcast is None:
            queryset = Release.objects.all()
        else:
            queryset = Release.objects.filter(podcast=podcast)
        news = get_object_or_404(queryset, pk=pk)
        serializer = ReleaseSerializer(news)
        data = serializer.data
        data['neigbours'] = []
        neigbours = news.get_neigbours()
        for neigbour in neigbours:
            serializer = ReleaseSerializer(neigbour)
            data['neigbours'].append(serializer.data)
        return Response(data)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer
    permission_classes = (IsAdminOrReadOnly, )
    paginate_by = 6
    paginate_by_param = 'count'


class ArtistItemViewSet(APIView):
    model = Artist

    def get(self, request, pk=None):
        queryset = Artist.objects.all()
        artist = get_object_or_404(queryset, pk=pk)
        serializer = ArtistSerializer(artist)
        data = serializer.data
        data['releases'] = []
        releases = artist.releases.all()[:4]
        for release in releases:
            serializer = ReleaseSerializer(release)
            data['releases'].append(serializer.data)
        return Response(data)
