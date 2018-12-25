# Register your models here.


from django.contrib import admin
from music.models import Performer, Song


admin.site.register(Performer)
admin.site.register(Song)
