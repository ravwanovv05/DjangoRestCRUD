from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=64)
    image = models.ImageField(_('Image'), upload_to='pics')
    description = models.TextField(_('Description'))

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

