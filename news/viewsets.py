from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NewsSerializer
from .models import News
from utils.permissions import IsAdminOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-create_date')
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly, )
    paginate_by = 10
    paginate_by_param = 'count'
