from django.contrib import admin
from release.models import Release, Artist, ArtistImage
from django.db import models
from embed_video.admin import AdminVideoMixin
from embed_video.fields import EmbedVideoField
from django.contrib.admin.widgets import AdminFileWidget
from django import forms
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin


class ArtistImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'img_image', )

    def img_image(self, obj):
        return '<img src="%s" style="max-height: 150px;"/>' % obj.image.url
    img_image.allow_tags=True
admin.site.register(ArtistImage, ArtistImageAdmin)


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value:
            output.append('<img src="/media/{}" style="max-width: 200px; max-height: 200px">' . format(value))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class GalleryImageForm(forms.ModelForm):

    class Meta:
        model = ArtistImage
        fields = ('image', )
        widgets = {
            'image' : AdminImageWidget,
        }

class ReleasesInline(admin.TabularInline):
    model = Release


class ImagesInline(admin.TabularInline):
    model = ArtistImage
    form = GalleryImageForm


class ArtistAdmin(SummernoteModelAdmin):
    list_display_links = ('id', )
    list_display = ('id', 'name', 'biography', )
    search_fields = ('name', 'biography', )
    list_editable = ()
    inlines = [
        ImagesInline,
        ReleasesInline,
    ]
admin.site.register(Artist, ArtistAdmin)


class ReleaseAdmin(SummernoteModelAdmin):
    list_display_links = ('id', )
    list_display = ('id', 'name', 'content', 'release', 'podcast', )
    search_fields = ('name', 'content', )
    list_editable = ()
admin.site.register(Release, ReleaseAdmin)
