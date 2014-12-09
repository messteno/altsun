from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework import routers
from .viewsets import UserViewSet
from .views import ProfileView, LogoutView, LoginView
from django.conf.urls.static import static
from django.conf import settings
from news.viewsets import NewsViewSet, NewsItemViewSet
from release.viewsets import ReleaseViewSet, ReleaseItemViewSet, ArtistViewSet, ArtistItemViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)
router.register(r'releases', ReleaseViewSet)
router.register(r'artists', ArtistViewSet)


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='altsun/index.html'),
        name='index'),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/profile/', ProfileView.as_view()),
    url(r'^api/logout/', LogoutView.as_view()),
    url(r'^api/login/', LoginView.as_view()),
    url(r'^api/news/item/(\d+)/', NewsItemViewSet.as_view()),
    url(r'^api/releases/item/(\d+)/', ReleaseItemViewSet.as_view()),
    url(r'^api/artists/item/(\d+)/', ArtistItemViewSet.as_view()),
    url(r'^api/', include(router.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
