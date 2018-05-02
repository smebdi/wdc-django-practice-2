from django.contrib import admin

from .models import Artist, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'artistic_name', 'first_name', 'last_name',)
