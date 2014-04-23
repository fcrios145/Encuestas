from django.conf.urls import patterns, include, url
from .views import index,genero, edad

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index.as_view(), name='home'),
    url(r'^genero$', genero.as_view(), name='genero'),
    url(r'^edad$', edad.as_view(), name='edad'),
    # url(r'^blog/', include('blog.urls')),


)
