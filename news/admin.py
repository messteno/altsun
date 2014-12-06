from django.contrib import admin
from news.models import News, NewsImage
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django import forms
from django.utils.safestring import mark_safe


class NewsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'img_image', )

    def img_image(self, obj):
        return '<img src="%s" style="max-height: 150px;"/>' % obj.image.url
    img_image.allow_tags=True
admin.site.register(NewsImage, NewsImageAdmin)


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value:
            output.append('<img src="/media/{}" style="max-width: 200px; max-height: 200px">' . format(value))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class GalleryImageForm(forms.ModelForm):

    class Meta:
        model = NewsImage
        fields = ('image', )
        widgets = {
            'image' : AdminImageWidget,
        }


class ImagesInline(admin.TabularInline):
    model = NewsImage
    form = GalleryImageForm


class NewsAdmin(admin.ModelAdmin):
    list_display_links = ('id', )
    list_display = ('id', 'title', 'content', 'create_date', )
    search_fields = ('title', 'content', )
    list_editable = ()
    inlines = [
        ImagesInline,
    ]
admin.site.register(News, NewsAdmin)
