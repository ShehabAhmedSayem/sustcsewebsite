from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('undergrad/major/', views.undergrad_major, name='umajor'),
    path('undergrad/second-major/', views.undergrad_second_major, name='usecmajor'),
    path('grad/major/', views.grad_major, name='gmajor'),
    path('grad/second-major/', views.grad_second_major, name='gsecmajor'),
    path('phd/', views.phd, name='phd'),
    path('ccna/', views.ccna, name='ccna'),
    path('publications/', views.publications, name='publications'),
]