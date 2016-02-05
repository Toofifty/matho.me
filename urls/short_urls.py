from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<short_url>.+)$', views.redir, name='redir'),
]