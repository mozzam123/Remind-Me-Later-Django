from django.db import models

# Create your models here.
from django.db import models

class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=255)
    reminder_method = models.CharField(max_length=10, choices=(('SMS', 'SMS'), ('Email', 'Email')))
