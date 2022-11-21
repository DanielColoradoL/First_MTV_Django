from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre_completo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    no_identidad = models.IntegerField()

    def __str__(self):
        return self.nombre_completo