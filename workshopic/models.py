from django.db import models
from django.utils import timezone
import  re
from django.db.models import Q

# Create your models here.
class Workshop(models.Model):
    workshopid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    occ_no = models.CharField(max_length=200)
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)
    location = models.CharField(max_length=200)
    man_no_part = models.BigIntegerField()
    num_of_facil = models.BigIntegerField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Participant(models.Model):
    participantid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    workshopid = models.ForeignKey(Workshop, on_delete= None)
    reg_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.reg_date = timezone.now()
        self.save()

    def __str__(self):
        return self.fname

class Facilitator(models.Model):
    facilitatorid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    workshopid = models.ForeignKey(Workshop, on_delete= None)
    reg_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.reg_date = timezone.now()
        self.save()

    def __str__(self):
        return self.fname

