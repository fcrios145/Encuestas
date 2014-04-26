from django.contrib import admin
from .models import Carrera,Pregunta,Respuesta,Catalogo,Persona

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Persona)
admin.site.register(Catalogo)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
