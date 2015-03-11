from django.db import models

# Create your models here.

class EntityLabel(models.Model):
    lang=models.CharField(max_length=10)
    entity_id=models.IntegerField()
    label=models.TextField(blank=True, null=True)
    def __unicode__(self):
        return str(self.entity_id)+" "+lang

class Artwork(models.Model):
    entity_id = models.IntegerField(primary_key=True) #instance
    p31 = models.IntegerField() #instance
    p135 = models.IntegerField(blank=True, null=True) # movement
    p136 = models.IntegerField(blank=True, null=True) # genre
    p170 = models.IntegerField(blank=True, null=True) # creator
    p195 = models.IntegerField(blank=True, null=True) #collection
    p18 = models.TextField(blank=True, null=True) #image
    def __unicode__(self):
        return str(self.entity_id)

class Artist(models.Model):
    entity_id = models.IntegerField(primary_key=True) #instance
    p21 = models.IntegerField(blank=True, null=True) #gender
    p27 = models.IntegerField(blank=True, null=True) #country of citizenship
    p732 = models.IntegerField(blank=True, null=True) #given name
    def __unicode__(self):
        return str(self.entity_id)
