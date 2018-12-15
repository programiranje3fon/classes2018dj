# Create your models here.

from django.db import models
from django.urls import reverse


class Performer(models.Model):

    musician_or_band = [
        [False, 'musician'],
        [True, 'band']
    ]

    name = models.CharField(max_length=100)
    is_band = models.BooleanField(verbose_name='Musician/Band',
                                  choices=musician_or_band,
                                  default=False)

    def __str__(self):
        return self.name + (' (band)' if self.is_band else ' (musician)')

    def get_absolute_url(self):
        return reverse('performer-detail', args=[str(self.id)])

