from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from curriculum.models import Program


def index(request):
    context = {}
    return render(request, 'home/index.html', context)


def about(request):
    context = {}
    return render(request, 'home/about.html', context)


def undergrad_major(request):
    program = Program.objects.get(program_name="Undergraduate Major")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def underegrad(request):
    context = {}
    return render(request, 'home/undergrad.html', context)


def undergrad_second_major(request):
    program = Program.objects.get(program_name="Undergraduate Second Major")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def masters(request):
    program = Program.objects.get(program_name="Masters")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def phd(request):
    program = Program.objects.get(program_name="Phd")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def ccna(request):
    program = Program.objects.get(program_name="CCNA")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def publications(request):
    context = {}
    return render(request, 'home/publications.html', context)
