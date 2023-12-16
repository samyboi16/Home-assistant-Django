from django.db import models

class User(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=16, null=False,blank=False)