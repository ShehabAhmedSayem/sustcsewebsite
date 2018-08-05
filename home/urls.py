from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account_redirect, name='account-redirect'),
    path('about/', views.about, name='about'),
    path('undergrad-major/', views.undergrad_major, name='umajor'),
    path('undergrad-second-major/', views.undergrad_second_major, name='usecmajor'),
    path('masters/', views.masters, name='masters'),
    path('phd/', views.phd, name='phd'),
    path('ccna/', views.ccna, name='ccna'),
]