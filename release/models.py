from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from utils import get_uuid_file_path


class Artist(models.Model):
    name = models.CharField(null=False, blank=False, max_length=512,
                             verbose_name=u'Имя')
    biography = models.TextField(null=False, blank=False,
                               verbose_name=u'Биография')

    class Meta:
        verbose_name = u'артист'
        verbose_name_plural = u'артисты'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


def get_artists_image_path(instance, filename):
    return get_uuid_file_path('artists', filename)



class ArtistImage(models.Model):
    image = models.ImageField(upload_to=get_artists_image_path, blank=False, null=False)
    preview_sm = ImageSpecField(source='image',
                                processors=[ResizeToFill(400, 250)],
                                format='JPEG',
                                options={'quality': 90})
    preview_md = ImageSpecField(source='image',
                                processors=[ResizeToFill(800, 500)],
                                format='JPEG',
                                options={'quality': 90})
    artist = models.ForeignKey(Artist, null=True, blank=True, related_name='images')

    class Meta:
        verbose_name = u'изображение артиста'
        verbose_name_plural = u'изображения артистов'

    def __str__(self):
        return self.image.url

    def __unicode__(self):
        return self.image.url


class Release(models.Model):
    name = models.CharField(null=False, blank=False, max_length=512,
                            verbose_name=u'Название')
    content = models.TextField(null=False, blank=False,
                               verbose_name=u'Содержание')
    create_date = models.DateTimeField(null=False, auto_now_add=True,
                                       default=timezone.now,
                                       verbose_name=u'Дата публикации')
    release = EmbedVideoField(verbose_name=u'Ссылка')
    podcast = models.BooleanField(default=False, verbose_name=u'Подкаст')
    artist = models.ForeignKey(Artist, null=True, blank=True, related_name='releases')

    class Meta:
        verbose_name = u'релизы и подкасты'
        verbose_name_plural = u'релизы и подкасты'

    def get_neigbours(self):
        prev_count = 2
        next_count = 2
        neigbours = list()
        neigbour = self
        for i in range(prev_count):
            try:
                neigbour = neigbour.get_previous_by_create_date(podcast=self.podcast)
                neigbours.insert(0, neigbour)
            except:
                pass
        neigbour = self
        for i in range(next_count):
            try:
                neigbour = neigbour.get_next_by_create_date(podcast=self.podcast)
                neigbours.append(neigbour)
            except:
                pass
        return neigbours

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
