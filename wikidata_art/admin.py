from django.contrib import admin
from wikidata_art.models import Artist, Artwork, EntityLabel

# Register your models here.
admin.site.register(Artist)
admin.site.register(Artwork)
admin.site.register(EntityLabel)
