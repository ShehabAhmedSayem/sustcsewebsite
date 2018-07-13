from django.urls import path

from . import views

urlpatterns = [
    path('faculty/', views.faculty, name='faculty'),
    path('faculty/<int:faculty_id>', views.faculty_detail, name='faculty_detail'),
    path('student/', views.student, name='student'),
    path('staff/', views.staff, name='staff'),
]