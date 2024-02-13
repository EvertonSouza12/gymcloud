from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class user(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, null=True, unique=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username