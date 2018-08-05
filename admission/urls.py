from django.urls import path

from . import views

urlpatterns = [
    path('second-major/', views.admission_second_major, name='admission_second_major'),
    path('second-major/application', views.second_major_application, name='second_major_application'),

    path('phd/', views.admission_phd, name='admission_phd'),

    path('masters/', views.admission_masters, name='admission_masters'),

    path('ccna/', views.admission_ccna, name='admission_ccna'),

]