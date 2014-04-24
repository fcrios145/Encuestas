from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from .models import Carrera
# Create your views here.

# def index(request):
#     return render_to_response('inicio/index.html')

class index(TemplateView):
    template_name = "inicio/index.html"

    # def get_context_data(self, **kwargs):
    #     context = super(index, self).get_context_data(**kwargs)
    #     self.request.session["fav_color"] = "blue"
    #     return context

class genero(TemplateView):
    template_name = 'inicio/sexo.html'




class edad(TemplateView):
    # def get_context_data(self, **kwargs):
    #     context = super(edad, self).get_context_data(**kwargs)
    #     self.request.session["genero"] =self.request.GET.get('g','h')
    #     return context
    def get(self, request, *args, **kwargs):
        genero = request.GET['genero']
        self.request.session["genero"] = genero
        print self.request.session["genero"]
        #

        datos = []
        valor = 15
        for x in range(15, 39):
            datos.append(
                dict(
                    [
                        ('edad', valor)
                    ]
                )
            )
            valor += 1
        return render_to_response('inicio/edad_ajax.html', {"edades": datos})
        # return render_to_response('inicio/edad_ajax.html')
        # return render_to_response('inicio/edad_ajax.html', {"data": "hola"})

class carrera(TemplateView):
    def get(self, request, *args, **kwargs):
        edad = request.GET['edad']
        self.request.session["edad"] = edad
        datos = Carrera.objects.all()
        return render_to_response('inicio/carrera.html', {'carreras': datos})
