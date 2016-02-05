from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20)
    built_with = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    src = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    img = models.CharField(max_length=50)
    
    def relevance(self, terms):
        rel = 0
        for term in terms:
            if term in self.built_with:
                rel += 2
            if term in self.description:
                rel += 1
        return rel