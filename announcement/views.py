from django.shortcuts import render, get_object_or_404
from .models import Notice


def notice(request):
    notices = Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'announcement/notice-board.html', context)


def news(request):
    context = {}
    return render(request, 'announcement/news-events.html', context)


def honor(request):
    context = {}
    return render(request, 'announcement/honor-board.html', context)
