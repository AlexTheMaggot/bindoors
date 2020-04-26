from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'mainapp/index.html', context)

def agreement(request):
    return render(request, 'mainapp/agreement.html')

def privacy(request):
    return render(request, 'mainapp/privacy.html')