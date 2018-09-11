from django.shortcuts import render, get_object_or_404
from .models import Notice, News, HonorBoard, Event


def notice(request):
    notices = Notice.objects.all().order_by('-date_published')
    context = {'notices': notices}
    return render(request, 'announcement/notice-board.html', context)


def news(request):
    news = News.objects.all().order_by('-date_published')
    context = {'news': news}
    return render(request, 'announcement/news.html', context)


def honor(request):
    honors = HonorBoard.objects.all()
    context = {'honors': honors}
    return render(request, 'announcement/honor-board.html', context)


def events(request):
    events = Event.objects.all().order_by('-event_date')
    context = {'events': events}
    return render(request, 'announcement/events.html', context)
