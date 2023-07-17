from django.db import models

class Tests(models.Model):
    title = models.CharField("Название теста", max_length=50)