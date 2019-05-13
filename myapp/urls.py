from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),

    path('clogin/', views.clogin, name='clogin'),
    path('signup/', views.signup, name='signup'),
    path('signupSubmit/', views.signupSubmit, name='signupSubmit'),
    path('loginSubmit/', views.loginSubmit, name='loginSubmit'),
    path('alogin/', views.alogin, name='alogin'),
    path('aloginSubmit/', views.aloginSubmit, name='aloginSubmit'),
    path('chome/', views.chome, name='chome'),
    path('ahome/', views.ahome, name='ahome'),
    path('add_fine/', views.add_fine, name='add_fine'),
    path('clear_fine/', views.clear_fine, name='clear_fine'),
    path('fine_look/', views.fine_look, name='fine_look'),
    path('calc/', views.calc_fine, name='calc_fine'),
]