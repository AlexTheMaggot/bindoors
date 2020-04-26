from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agreement/', views.agreement, name='agreement'),
    path('privacy/', views.privacy, name='privacy'),
]