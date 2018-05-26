from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    context = {}
    return render(request, 'home/index.html', context)


def about(request):
    context = {}
    return render(request, 'home/about.html', context)


def undergrad_major(request):
    context = {}
    return render(request, 'home/undergrad_major.html', context)


def undergrad_second_major(request):
    context = {}
    return render(request, 'home/undergrad_second_major.html', context)


def grad_major(request):
    context = {}
    return render(request, 'home/grad_major.html', context)


def grad_second_major(request):
    context = {}
    return render(request, 'home/grad_second_major.html', context)


def phd(request):
    context = {}
    return render(request, 'home/phd.html', context)


def ccna(request):
    context = {}
    return render(request, 'home/ccna.html', context)