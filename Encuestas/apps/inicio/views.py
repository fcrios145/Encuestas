from django.http import HttpResponse
from django.views.generic import TemplateView
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
    template_name = 'inicio/edad.html'
    def get_context_data(self, **kwargs):
        context = super(edad, self).get_context_data(**kwargs)
        self.request.session["genero"] =self.request.GET.get('g','h')
        return context
