from django.urls import path
from . import views



urlpatterns = [
    path('', views.recruitment_form, name='recruitment_form'),
    path('thank/', views.thank, name='thank'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
