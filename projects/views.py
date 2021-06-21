from django.shortcuts import render

from .models import project

def index(request):
    projects = project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/index.html', context)
    
def detail(request, pk):
    projects = project.objects.get(pk=pk)
    context = {
        'project': projects
    }
    return render(request, 'projects/detail.html', context)

