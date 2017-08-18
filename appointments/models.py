from django.db import models
import datetime
import json
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core import serializers
import logging

logr = logging.getLogger(__name__) 

class Appointment(models.Model):
    host = models.ForeignKey('Host')
    customer = models.CharField(max_length = 200)
    reason = models.CharField(max_length = 500)
    start_time = models.DateTimeField((u"Appointment Start"))
    end_time = models.DateTimeField((u"Appointment End"))
    
    def __unicode__(self):
        return unicode(self.customer + ":" + self.reason)


class Host(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return unicode(self.firstname + self.middlename + self.lastname)