from django.db import models

class data(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)