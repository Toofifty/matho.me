from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/(?P<long_url>.+)$', views.new, name='new'),
    url(r'^remove/(?P<short_url>.+)$', views.remove, name='remove'),
]