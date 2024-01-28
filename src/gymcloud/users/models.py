from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    cpf = models.CharField(max_length=11, unique=True,)
    data_nascimento = models.DateField()
    
    
# class Workout(models.Model):
#     pass