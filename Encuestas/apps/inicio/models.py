from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='imagen_carrera')

    def __unicode__(self):
        return self.nombre

class Catalogo(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField(blank=True)


class Pregunta(models.Model):
    texto = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='imagen_preguntas')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    catalogo = models.ForeignKey(Catalogo)

    def __unicode__(self):
        return self.texto

class Persona(models.Model):
    carrera = models.ForeignKey(Carrera)
    genero = models.BooleanField(default=True)
    edad = models.IntegerField()

class Respuesta(models.Model):
    texto = models.TextField()
    imagen = models.ImageField(upload_to='imagen_respuestas')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pregunta = models.ForeignKey(Pregunta)

    def __unicode(self):
        return self.texto

class Dato(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    persona = models.OneToOneField(Persona)

