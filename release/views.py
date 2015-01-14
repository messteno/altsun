from django.shortcuts import render
from release.forms import ReleaseDownloadForm
from utils.mixins import AjaxCapableProcessFormViewMixin
from utils import get_media_url_path
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.template import Context
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from .models import Release, Artist
from .serializers import ReleaseSerializer, ArtistSerializer


class ReleaseItemView(APIView):
    model = Release

    def get(self, request, pk=None):
        podcast = request.GET.get('podcast')
        if podcast is None:
            queryset = Release.objects.all()
        else:
            queryset = Release.objects.filter(podcast=podcast)
        news = get_object_or_404(queryset, pk=pk)
        serializer = ReleaseSerializer(release)
        data = serializer.data
        data['neigbours'] = []
        neigbours = news.get_neigbours()
        for neigbour in neigbours:
            serializer = ReleaseSerializer(neigbour)
            data['neigbours'].append(serializer.data)
        return Response(data)


class ArtistItemView(APIView):
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


class ReleaseDownloadView(AjaxCapableProcessFormViewMixin, FormView):
    form_class = ReleaseDownloadForm
    template_name = 'altsun/releases/download.html'

    def form_valid(self, form):
        form.save()
        subject = 'Ссылка на релиз от Alter Native Sun'
        from_email = getattr(settings, 'DEMO_EMAIL', 'info@alt-sun.com')
        to = form.cleaned_data['email']
        release = form.cleaned_data['release']
        context = Context({
            'release': release.name,
            'url': self.request.build_absolute_uri(release.archive.url)
        })
        text_content = render_to_string('altsun/mail/release.txt', context)
        html_content = render_to_string('altsun/mail/release.html', context)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
