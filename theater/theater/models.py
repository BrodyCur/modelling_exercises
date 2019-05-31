from django.db import models

class Actor(models.Model):
  name = models.CharField(max_length=255)

class Director(models.Model):
  name = models.CharField(max_length=255)

class Play(models.Model):
  title = models.CharField(max_length=255)
  writer = models.CharField(max_length=255)
  director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='plays')
  actor = models.ManyToManyField(Actor, through='Role', related_name='roles')

class Role(models.Model):
  name = models.CharField(max_length=255)
