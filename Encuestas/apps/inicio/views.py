from django.views.generic import TemplateView
# Create your views here.

# def index(request):
#     return render_to_response('inicio/index.html')

class index(TemplateView):
    template_name = 'inicio/index.html'
