from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class meeting(models.Model):
    meetingtitle=models.CharField(max_length=220)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=254)
    agenda=models.TextField()

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'

class meetingminute(models.Model):
    meetingid=models.ForeignKey(meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField

    def __str__(self):
        return self.meetingid
    class Meta:
        db_table='meetingminutes'

class resource(models.Model):
    resourcename=models.CharField(max_length=254)
    resourcetype=models.CharField(max_length=254)
    resourceurl=models.URLField()
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'

class event(models.Model):
    eventname=models.CharField(max_length=254)
    eventlocation=models.CharField(max_length=300)
    eventdate=models.DateField()
    eventtime=models.DateTimeField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventname

    class Meta:
        db_table='event'


    
