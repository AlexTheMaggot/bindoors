import telebot

from django.views import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import Project, Partner, Review
from .forms import RecallForm, SendCatalogForm, SendCatandpriceForm, QuizForm, SubscribeForm

bot = telebot.TeleBot("1168539036:AAFt31_hCwD7Vds8m-2Aivzhxq3U6hDRTCc")


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
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                subject = 'Новая заявка на обратный звонок'
                from_email = 'no-reply@bindoors.ru'
                to_email = ['info@bindoors.ru', 'i.bulychev@bindoors.ru',]
                message = 'Новая заявка на обратный звонок!' + '\r\n' + '\r\n' + 'Имя: ' + name + '\r\n'
                message += 'Телефон: ' + phone

                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(-1001204503517, message)
                return redirect('/recall/thank-you')
        return redirect('/wrong')


class SendCatalogView(View):

    def post(self, request):
        if request.method == 'POST':
            form = SendCatalogForm(request.POST)
            if form.is_valid():
                form.save()
                mail = form.cleaned_data['mail']
                subject = 'Новая заявка на отправку каталога!'
                from_email = 'no-reply@bindoors.ru'
                to_email = ['info@bindoors.ru', 'i.bulychev@bindoors.ru',]
                message = 'Новая заявка на отправку каталога!' + '\r\n' + '\r\n' + 'Почта: ' + mail

                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(-1001204503517, message)
                return redirect('/send-catalog/thank-you')
        return redirect('/wrong')


class SendCatandpriceView(View):
    def post(self, request):
        if request.method == 'POST':
            form = SendCatandpriceForm(request.POST)
            if form.is_valid():
                form.save()
                mail = form.cleaned_data['mail']
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                subject = 'Новая заявка на отправку каталога и прайса!'
                from_email = 'no-reply@bindoors.ru'
                to_email = ['info@bindoors.ru', 'i.bulychev@bindoors.ru',]
                message = 'Новая заявка на отправку каталога и прайса!' + '\r\n' + '\r\n' + 'Имя: ' + name
                message += '\r\n' + 'Телефон: ' + phone + '\r\n' + 'Почта: ' + mail

                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(-1001204503517, message)

                return redirect('/send-catalog-price/thank-you')
        return redirect('/wrong')


class QuizView(View):
    def post(self, request):
        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                form.save()
                door_type = form.cleaned_data['door_type']
                price_type = form.cleaned_data['price_type']
                style_type = form.cleaned_data['style_type']
                size_type = form.cleaned_data['size_type']
                material_type = form.cleaned_data['material_type']
                mail = form.cleaned_data['mail']
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                subject = 'Новая заявка с квиза!'
                from_email = 'no-reply@bindoors.ru'
                to_email = ['info@bindoors.ru', 'i.bulychev@bindoors.ru',]
                message = 'Новая заявка с квиза!' + '\r\n' + '\r\n' + 'Имя: ' + name
                message += '\r\n' + 'Телефон: ' + phone + '\r\n' + 'Почта: ' + mail
                message += '\r\n' + '\r\n' + 'Тип двери: ' + door_type + '\r\n'
                message += 'Ценовой сегмент: ' + price_type + '\r\n' + 'Стиль: ' + style_type + '\r\n'
                message += 'Размер: ' + size_type + '\r\n' + 'Материал: ' + material_type

                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(-1001204503517, message)

                return redirect('/quiz/thank-you')
        return redirect('/wrong')


class SubscribeView(View):
    def post(self, request):
        if request.method == 'POST':
            form = SubscribeForm(request.POST)
            if form.is_valid():
                form.save()
                mail = form.cleaned_data['mail']
                subject = 'Новая заявка на подписку!'
                from_email = 'no-reply@bindoors.ru'
                to_email = ['info@bindoors.ru', 'i.bulychev@bindoors.ru',]
                message = 'Новая заявка на подписку!' + '\r\n' + '\r\n' + 'Почта: ' + mail

                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(-1001204503517, message)
                return redirect('/subscribe/thank-you')
        return redirect('/wrong')


def agreement(request):
    return render(request, 'mainapp/agreement.html')


def privacy(request):
    return render(request, 'mainapp/privacy.html')


def thank_you(request):
    return render(request, 'mainapp/thank-you.html')


def wrong(request):
    return render(request, 'mainapp/wrong.html')


def custom_404(request, exception):
    return render(request, "mainapp/404.html")
