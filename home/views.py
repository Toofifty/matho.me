from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})
    
def about(request):
    return render(request, 'home/about.html', {})
    
def projects(request, search_term):
    return render(request, 'home/ph_projects.html', {})