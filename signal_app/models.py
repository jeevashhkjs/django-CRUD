from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.

class Users(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    number = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name


class UserScore(models.Model) :
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=True, blank=True)

    def __str__(self) :
        return str(self.number)