from django.db import models


class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField()