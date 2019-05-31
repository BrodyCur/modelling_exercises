from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=255)

class Writer(models.Model):
  name = models.CharField(max_length=255)

class Comic(models.Model):
  title = models.CharField(max_length=255)

class Issue(models.Model):
  number = models.IntegerField()
  comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='issues')
  artist = models.ManyToManyField(Artist)
  writer = models.ManyToManyField(Writer)