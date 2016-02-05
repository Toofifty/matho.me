from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^projects/(?P<search_term>)', views.projects, name='projects'),
    url(r'^projects/', views.projects, name='projects')
]