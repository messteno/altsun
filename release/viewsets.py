from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from utils.permissions import IsAdminOrReadOnly
from .serializers import ReleaseSerializer, ArtistSerializer
from .models import Release, Artist


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all().order_by('-create_date')
    serializer_class = ReleaseSerializer
    permission_classes = (IsAdminOrReadOnly, )
    paginate_by = 6
    paginate_by_param = 'count'
    filter_fields = ('podcast', )


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer
    permission_classes = (IsAdminOrReadOnly, )
    paginate_by = 6
    paginate_by_param = 'count'
