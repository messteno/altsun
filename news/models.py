#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from utils import get_uuid_file_path


class News(models.Model):
    title = models.CharField(null=False, blank=False, max_length=512,
                             verbose_name=u'Название')
    content = models.TextField(null=False, blank=False,
                               verbose_name=u'Содержание')
    create_date = models.DateTimeField(null=False, auto_now_add=True,
                                       default=timezone.now,
                                       verbose_name=u'Дата публикации')

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'

    def get_neigbours(self):
        prev_count = 2
        next_count = 2
        neigbours = list()
        neigbour = self
        for i in range(prev_count):
            try:
                neigbour = neigbour.get_previous_by_create_date()
                neigbours.insert(0, neigbour)
            except:
                pass
        neigbour = self
        for i in range(next_count):
            try:
                neigbour = neigbour.get_next_by_create_date()
                neigbours.append(neigbour)
            except:
                pass
        return neigbours

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def get_news_image_path(instance, filename):
    return get_uuid_file_path('news', filename)


class NewsImage(models.Model):
    image = models.ImageField(upload_to=get_news_image_path, blank=False, null=False)
    preview_sm = ImageSpecField(source='image',
                                processors=[ResizeToFill(400, 250)],
                                format='JPEG',
                                options={'quality': 90})
    preview_md = ImageSpecField(source='image',
                                processors=[ResizeToFill(800, 500)],
                                format='JPEG',
                                options={'quality': 90})
    news = models.ForeignKey(News, null=True, blank=True, related_name='images')

    class Meta:
        verbose_name = u'изображение новости'
        verbose_name_plural = u'изображения новостей'

    def __str__(self):
        return self.image.url

    def __unicode__(self):
        return self.image.url
