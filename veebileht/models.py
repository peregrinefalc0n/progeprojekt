from django.db import models

#Create your models here.

#Event class is defined here as a class/model
class Event(models.Model):
    name = models.TextField()
    time = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)

#addEvent(name, starttime, endtime = None, description = None, participants = None):

