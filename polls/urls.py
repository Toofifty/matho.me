from django.conf.urls import url

from . import views

# all sub-pages of polls/ as set
# in project/urls.py

urlpatterns = [
    # ^$ is a regex that parses into an empty string
    # ^ is start, $ is end
    # GET vars are not checked (i.e /polls/?id=5 passes
    # to /polls/)
    
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.details, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]