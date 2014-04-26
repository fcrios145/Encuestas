from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='imagen_carrera')

    def __unicode__(self):
        return self.nombre



class Respuesta(models.Model):
    texto = models.TextField()
    imagen = models.ImageField(upload_to='imagen_respuestas')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.texto


class Pregunta(models.Model):
    texto = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='imagen_preguntas')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    respuestas = models.ManyToManyField(Respuesta)

    def __unicode__(self):
        return self.texto

class Catalogo(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField(blank=True)
    preguntas = models.ManyToManyField(Pregunta)

    def __unicode__(self):
        return self.nombre

class Persona(models.Model):
    carrera = models.ForeignKey(Carrera)
    genero = models.BooleanField(default=True)
    edad = models.IntegerField()

