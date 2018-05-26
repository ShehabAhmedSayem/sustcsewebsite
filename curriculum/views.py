from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Curriculum

def undergrad_major(request):
    curriculum = Curriculum.objects.get(program_name='Undergrad_major')
    context = {'curriculum': curriculum}
    return render(request, 'curriculum/undergrad_major.html', context)


def undergrad_second_major(request):
    context = {}
    return render(request, 'curriculum/undergrad_second_major.html', context)


def grad_major(request):
    context = {}
    return render(request, 'curriculum/grad_major.html', context)


def grad_second_major(request):
    context = {}
    return render(request, 'curriculum/grad_second_major.html', context)


def phd(request):
    context = {}
    return render(request, 'curriculum/phd.html', context)


def ccna(request):
    context = {}
    return render(request, 'curriculum/ccna.html', context)