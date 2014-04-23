from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

# def index(request):
#     return render_to_response('inicio/index.html')

class index(TemplateView):
    template_name = "inicio/index.html"

    # def get_context_data(self, **kwargs):
    #     context = super(index, self).get_context_data(**kwargs)
    #     # context['latest_articles'] = Article.objects.all()[:5]
    #     self.request.session["fav_color"] = "blue"
    #     return context


