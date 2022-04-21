from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('save/', views.save, name='save'),
    path('login/', views.login, name='login'),
    path('firstPage/', views.firstPage, name='firstPage')
]