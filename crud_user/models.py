from django.db import models

from django.db import models

class usuarios(models.Model):
    username = models.TextField(max_length = 100)
    passwd = models.CharField(max_length = 100)
    