from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Curriculum


def undergrad_major(request):
    curriculum = Curriculum.objects.get(program_name='Undergrad_major')
    context = {'curriculum': curriculum}
    return render(request, 'curriculum/curriculum.html', context)


def undergrad_second_major(request):
    curriculum = Curriculum.objects.get(program_name='Undergrad_second_major')
    context = {'curriculum': curriculum}
    return render(request, 'curriculum/curriculum.html', context)


def grad_major(request):
    curriculum = Curriculum.objects.get(program_name='Grad_major')
    context = {'curriculum': curriculum}
    return render(request, 'curriculum/curriculum.html', context)


def grad_second_major(request):
    curriculum = Curriculum.objects.get(program_name='Grad_second_major')
    context = {'curriculum': curriculum}
    return render(request, 'curriculum/curriculum.html', context)


def phd(request):
    curriculum = Curriculum.objects.get(program_name='Phd')
    context = {'curriculum': curriculum}
    return render(request, 'curriculum/curriculum.html', context)


def ccna(request):
    curriculum = Curriculum.objects.get(program_name='CCNA')
    context = {'curriculum': curriculum}
    return render(request, 'curriculum/curriculum.html', context)
