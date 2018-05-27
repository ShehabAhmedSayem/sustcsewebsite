from django.urls import path

from . import views

urlpatterns = [
    path('notice-board/', views.notice, name='notice_board'),
    path('news-events/', views.news, name='news_events'),
    path('honor-board/', views.honor, name='honor_board'),
]