from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=255)

class Reader(models.Model):
  name = models.CharField(max_length=255)

class Book(models.Model):
  title = models.CharField(max_length=255)
  year = models.IntegerField()
  reader = models.ManyToManyField(Reader)
  author = models.ManyToManyField(Author)

class Chapter(models.Model):
  title = models.CharField(max_length=255)
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
