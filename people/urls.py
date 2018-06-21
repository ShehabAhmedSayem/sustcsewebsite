from django.urls import path

from . import views

urlpatterns = [
    path('faculty/', views.faculty, name='faculty'),
    path('student/', views.student, name='student'),
    path('staff/', views.staff, name='staff'),
]