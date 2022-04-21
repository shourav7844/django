from django.urls import path
from parking_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('save/', views.save, name='save'),
    path('user/', views.redirect_url, name='redirect_url'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('firstPage/', views.firstPage, name='firstPage')
]