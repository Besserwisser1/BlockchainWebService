from django.db import models

class Networks(models.Model):
    name = models.CharField(max_length=255)
    is_actual = models.BooleanField(default=True)

# class Contracts(models.Model):
#     address = models.CharField(max_length=255)
#     deployDate = models.DateField(auto_now=True)
#     deployUser = models.CharField(max_length=255)
#     contractFile = models.FileField()
#     abi = models.CharField(max_length=1000)
#     is_actual = models.BooleanField(default=True)

