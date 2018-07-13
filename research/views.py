from django.shortcuts import render, get_object_or_404
from .models import *


def research_groups(request):
    groups = ResearchGroup.objects.all()
    context={'groups': groups}
    return render(request, 'research/groups.html', context)


def publications(request):
    context={}
    return render(request, 'research/publications.html', context)
