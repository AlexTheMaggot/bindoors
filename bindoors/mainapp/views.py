from django.views import View
from django.shortcuts import render, redirect

from .models import Project, Partner, Review
from .forms import RecallForm, SendCatalogForm, SendCatandpriceForm, QuizForm, SubscribeForm


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


class RecallView(View):

    def post(self, request):
        if request.method == 'POST':
            form = RecallForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/thank-you')
        return redirect('/privacy')


class SendCatalogView(View):

    def post(self, request):
        if request.method == 'POST':
            form = SendCatalogForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/thank-you')
        return redirect('/privacy')


class SendCatandpriceView(View):
    def post(self, request):
        if request.method == 'POST':
            form = SendCatandpriceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/thank-you')
        return redirect('/privacy')


class QuizView(View):
    def post(self, request):
        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/thank-you')
        return redirect('/privacy')


class SubscribeView(View):
    def post(self, request):
        if request.method == 'POST':
            form = SubscribeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/thank-you')
            return redirect('/agreement')
        return redirect('/privacy')


def agreement(request):
    return render(request, 'mainapp/agreement.html')


def privacy(request):
    return render(request, 'mainapp/privacy.html')


def thank_you(request):
    return render(request, 'mainapp/thank-you.html')
