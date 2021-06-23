from django.shortcuts import render

from .models import about_person

def about(request):
    About_programer = about_person.objects.all().order_by('-create_on')
    context ={
        'About_programer': About_programer
    }
    return render(request, 'abouts/about.html', context)

def id_person(request,pk):
    Programer_id = about_person.objects.get(pk=pk)
    context = {
        'id' : Programer_id
    }
    return render(request, 'abouts/id_person.html', context)

