from django.db import models

#Create your models here.

#Event class is defined here as a class/model
class Event(models.Model):
    name = models.TextField()
    starttime = models.IntegerField()
    endtime = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    participants = models.IntegerField(blank=True, null=True)

#addEvent(name, starttime, endtime = None, description = None, participants = None):
