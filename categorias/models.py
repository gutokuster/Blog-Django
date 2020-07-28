from django.db import models


class Categorias(models.Model):
    nome_cat = models.CharField(max=50)
