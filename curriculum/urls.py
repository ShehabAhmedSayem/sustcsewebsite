from django.urls import path

from . import views

urlpatterns = [
    path('undergrad-major/', views.undergrad_major, name='cumajor'),
    path('undergrad-second-major/', views.undergrad_second_major, name='cusecmajor'),
    path('masters/', views.masters, name='cmasters'),
    path('phd/', views.phd, name='cphd'),
    path('ccna/', views.ccna, name='ccna'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('download-syllabus/<path:path>', views.download_syllabus, name='download_syllabus'),
]