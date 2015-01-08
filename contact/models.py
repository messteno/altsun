from django.db import models


class Contact(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)

    class Meta:
        verbose_name = u'контакт'
        verbose_name_plural = u'контакты'

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email
