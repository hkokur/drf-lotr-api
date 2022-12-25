from django.db import models


class Character(models.Model):
    """
    A model that record the characters in middle earth.
    Name and race mandolatory to record.
    """

    name = models.CharField(max_length=200)
    race = models.CharField(max_length=200)
    birth = models.CharField(blank=True, max_length=200)
    gender = models.CharField(blank=True, max_length=200)
    death = models.CharField(blank=True, max_length=200)
    hair = models.CharField(blank=True, max_length=200)
    height = models.CharField(blank=True, max_length=200)
    realm = models.CharField(blank=True, max_length=200)
    spouse = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.name
