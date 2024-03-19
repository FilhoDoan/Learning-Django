from django.db import models

class UserModel(models.Model):
    nome = models.CharField(max_length = 20)
    idade = models.IntegerField()
    cpf = models.IntegerField()

    


