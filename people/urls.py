from django.urls import path

from . import views

urlpatterns = [
    path('faculty/', views.faculty, name='faculty'),
    path('faculty/edit', views.update_faculty, name='update_faculty'),
    path('faculty/add_education', views.add_education, name='add_education'),
    path('faculty/<int:user_id>', views.faculty_detail, name='faculty_detail'),
    path('student/', views.student, name='student'),
    path('staff/', views.staff, name='staff'),
]