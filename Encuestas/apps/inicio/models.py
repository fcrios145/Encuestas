from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='imagen_carrera')

    def __unicode__(self):
        return self.nombre
