from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


def undergrad_major(request):
    program = Program.objects.get(program_name="Undergraduate Major")
    #course = program.course__set
    context = {'program': program}
    return render(request, 'curriculum/curriculum.html', context)


def undergrad(request):
    context = {}
    return render(request, 'home/undergrad.html', context)


def undergrad_second_major(request):
    program = Course.objects.get(program_name="Undergraduate Second Major")
    context = {'program': program}
    return render(request, 'curriculum/curriculum.html', context)


def masters(request):
    program = Course.objects.get(program_name="Masters")
    context = {'program': program}
    return render(request, 'curriculum/curriculum.html', context)


def phd(request):
    program = Course.objects.get(program_name="Phd")
    context = {'program': program}
    return render(request, 'curriculum/curriculum.html', context)


def ccna(request):
    program = Course.objects.get(program_name="CCNA")
    context = {'program': program}
    return render(request, 'curriculum/curriculum.html', context)
