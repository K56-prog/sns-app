from django.db import models

class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField(upload_to='')
    author = models.CharField(max_length=100)
    read = models.IntegerField(null=True, blank=True, default=1)
    good = models.IntegerField(null=True, blank=True, default=1)
    readers = models.TextField(null=True, blank=True, default='a')