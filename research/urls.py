from django.urls import path

from . import views

urlpatterns = [
    path('groups/', views.research_groups, name='research_groups'),
    path('publications/', views.publications, name='publications'),
]