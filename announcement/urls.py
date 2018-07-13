from django.urls import path

from . import views

urlpatterns = [
    path('notice-board/', views.notice, name='notice_board'),
    path('news/', views.news, name='news'),
    path('events/', views.events, name='events'),
    path('honor-board/', views.honor, name='honor_board'),
]