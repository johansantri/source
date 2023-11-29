from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Partner(models.Model):
    partner_name = models.TextField(max_length=191)
    partner_abbreviation = models.TextField(max_length=50)
    partner_email = models.ForeignKey(User,on_delete=models.CASCADE,related_name='partner_add')
    partner_phone = models.TextField(max_length=50)
    partner_address = models.TextField(max_length=50)
    partner_tax = models.TextField(max_length=50)
    partner_status = models.TextField(max_length=50)
    partner_check = models.TextField(max_length=50)
    partner_logo = models.ImageField(upload_to=filepath,null=True, blank=True)
    partner_join = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.partner_name}"



