from django.db import models

class Film(models.Model):
  title = models.CharField(max_length=255)
  year = models.IntegerField()

class Viewer(models.Model):
  name = models.CharField(max_length=255)
  age = models.IntegerField()
  film = models.ManyToManyField(Film)