from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_lenght=30)
    last_name = models.CharField(max_lenght=30)
    email = models.EmailField(max_lenght=254)
    cpf = models.CharField(max_lenght=11, unique=True,)
    data_nascimento = models.DateField()