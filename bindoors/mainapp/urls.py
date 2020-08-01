from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recall/', views.RecallView.as_view(), name='recall'),
    path('sendcatalog/', views.SendCatalogView.as_view(), name='sendcatalog'),
    path('sendcatandprice/', views.SendCatandpriceView.as_view(), name='sendcatandprice'),
    path('quiz/', views.QuizView.as_view(), name='quiz'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('agreement/', views.agreement, name='agreement'),
    path('privacy/', views.privacy, name='privacy'),
    path('send-catalog/thank-you/', views.thank_you, name='send-catalog-thank-you'),
    path('send-catalog-price/thank-you/', views.thank_you, name='send-catalog-price-thank-you'),
    path('quiz/thank-you/', views.thank_you, name='quiz-thank-you'),
    path('subscribe/thank-you/', views.thank_you, name='subscribe-thank-you'),
    path('recall/thank-you/', views.thank_you, name='recall-thank-you'),
    path('wrong/', views.wrong, name='wrong'),
]
