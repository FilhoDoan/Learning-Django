from django.db import models

class UserModel(models.Model):
    nome = models.CharField(max_length = 20)
    idade = models.IntegerField()
    cpf = models.IntegerField()

    def __str__(self):
        return f'Nome : {self.nome} | Idade : {self.idade} | CPF : {self.cpf}' 
