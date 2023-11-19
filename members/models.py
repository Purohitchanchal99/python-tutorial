# members/models.py

from django.db import models
from django.db import models

from django.utils import timezone
class Member(models.Model):
    topic_name = models.CharField(max_length=555)
    
    description = models.CharField(max_length=1500, default="Your default description here")

class Flow(models.Model):
    topic_name = models.CharField(max_length=555)
    
    description = models.CharField(max_length=1500, default="Your default description here")

class Oops(models.Model):
    topic_name = models.CharField(max_length=555)
    
    description = models.CharField(max_length=1500, default="Your default description here")

class Function(models.Model):
    topic_name = models.CharField(max_length=555)
    description = models.CharField(max_length=1500, default="Your default description here")

      
    
    
    
    
    
    