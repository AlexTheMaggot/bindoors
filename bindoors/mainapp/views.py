from django.shortcuts import render
from .models import Project, Partner, Review


def index(request):
    projects = Project.objects.all()
    partners = Partner.objects.all()
    reviews = Review.objects.all()
    context = {
        'projects': projects,
        'partners': partners,
        'reviews': reviews,
    }
    return render(request, 'mainapp/index.html', context)

def agreement(request):
    return render(request, 'mainapp/agreement.html')

def privacy(request):
    return render(request, 'mainapp/privacy.html')