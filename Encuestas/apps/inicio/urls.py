from django.conf.urls import patterns, include, url
from .views import index,genero

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index.as_view(), name='home'),
    url(r'^genero$', genero.as_view(), name='genero'),
    # url(r'^blog/', include('blog.urls')),


)
