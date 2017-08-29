from django.db import models


class Channel(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):

    channel = models.ForeignKey(Channel)
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
