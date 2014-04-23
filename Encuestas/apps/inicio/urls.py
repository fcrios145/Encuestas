from django.conf.urls import patterns, include, url
from .views import index

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),


)
