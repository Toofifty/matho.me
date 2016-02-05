from django.db import models
from django.contrib.auth.models import User

class UrlRecord(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.CharField(max_length=400)
    redirects = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    
    # Get the website name from the long_url
    def redirect_to(self):
        try:
            return self.no_http().split('/', 1)[0]
        except:
            return "null"
            
    # Remove http/s and www from the long_url
    def no_http(self):
        return self.long_url.replace('http://', '').replace(
            'https://', '').replace('www.', '')