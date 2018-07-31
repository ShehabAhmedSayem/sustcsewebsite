from django.urls import path

from . import views

urlpatterns = [
    path('faculty/', views.faculty, name='faculty'),
    path('faculty/<int:user_id>', views.faculty_detail, name='faculty_detail'),
    path('faculty/edit', views.update_faculty, name='update_faculty'),

    path('faculty/add_education', views.add_education, name='add_education'),
    path('faculty/delete_education/<int:education_id>', views.delete_education, name='delete_education'),

    path('faculty/add_experience', views.add_experience, name='add_experience'),
    path('faculty/delete_experience/<int:experience_id>', views.delete_experience, name='delete_experience'),

    path('faculty/add_publication', views.add_publication, name='add_publication'),
    path('faculty/delete_publication/<int:publication_id>', views.delete_publication, name='delete_publication'),

    path('faculty/add_social_profile', views.add_social_profile, name='add_social_profile'),
    path('faculty/delete_publication/<int:publication_id>', views.delete_publication, name='delete_publication'),

    path('faculty/add_award', views.add_award, name='add_award'),
    path('faculty/delete_award/<int:award_id>', views.delete_award, name='delete_award'),

    path('student/', views.student, name='student'),
    path('staff/', views.staff, name='staff'),
]