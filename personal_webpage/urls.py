from django.conf.urls import include, url
from django.contrib import admin

# list of pages that won't trigger 
# the redirect app 
pages = [
    'admin',
    'polls',
    'short',
]

# compile pages into regex
urls_regex = r'^' + r''.join(['(?!' + page + ')' for page in pages])

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^', include('home.urls', namespace='home')),
    url(urls_regex, include('urls.short_urls', namespace='short_urls')),
    url(r'^short/', include('urls.urls', namespace='urls')),
]
