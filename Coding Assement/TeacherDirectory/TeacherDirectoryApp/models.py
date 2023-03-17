from django.db import models

# Create your models here.

class TeachersInformation(models.Model):
    first_name = models.TextField(null=True,blank=True)
    second_name = models.TextField(null=True,blank=True)
    profile_picture = models.TextField(null=True,blank=True)
    email_address = models.TextField(null=True,blank=True,unique=True)
    phone_number = models.TextField(null=True,blank=True)
    room_number = models.TextField(null=True,blank=True)
    subjects_taught = models.TextField(null=True,blank=True)
    class Meta:
        db_table = "teachers_information"
