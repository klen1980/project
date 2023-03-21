from django.shortcuts import render
from .models import Project

def poject_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context )

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def home(request):
    return render(request, 'home.html')



# Create your views here.
