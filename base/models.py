from django.db import models


class Person(models.Model):
    first_last_name = models.CharField(max_length=255)


class Vacation(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='person'
    )
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    many = models.IntegerField(null=True, blank=True)
