# Create your models here.
import datetime
from time import strftime

from django.db import models
from django.urls import reverse


class Performer(models.Model):
    """The model representing performers.
    """

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
        """Returns the URL to access a particular performer instance.
        Enables specific Performer pages in admin to include "View on site" button.
        """

        return reverse('performer-detail', args=[str(self.id)])


class Song(models.Model):
    """The model representing songs.
    """

    title = models.CharField(max_length=100)
    performer = models.ForeignKey(Performer, blank=True, null=True, on_delete=models.SET_NULL)
    time = models.TimeField(null=True, blank=True, default=datetime.time(minute=3, second=0))
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'song: ' + self.title + '\n' + \
               '\t' + 'performer: ' + str(self.performer) + '\n' + \
               '\t' + 'time: ' + self.format_time() + '\n' + \
               '\t' + 'release date: ' + self.format_date()

    def format_time(self):
        return self.time.strftime('%#M:%S') if isinstance(self.time, datetime.time) else 'unknown'

    def format_date(self):
        return self.release_date.strftime('%b %d, %Y') if isinstance(self.release_date, datetime.date) else 'unknown'

    def get_absolute_url(self):
        """Returns the URL to access a particular song instance.
        Enables specific Song pages in admin to include "View on site" button.
        """

        return reverse('song-detail', args=[str(self.id)])

