from django.shortcuts import render

from projects.models import project

def presentation(request,):
    projects = project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'pageprincipals/index.html', context)
