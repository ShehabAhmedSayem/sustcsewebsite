from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


def undergrad_major(request):
    program = Program.objects.get(program_name="Undergraduate Major")
    courses = program.course_set.all()
    semesters = Semester.objects.all()
    context = {'program': program, 'courses': courses, 'semesters':semesters}
    return render(request, 'curriculum/curriculum.html', context)


def undergrad(request):
    context = {}
    return render(request, 'home/undergrad.html', context)


def undergrad_second_major(request):
    program = Program.objects.get(program_name="Undergraduate Second Major")
    courses = program.course_set.all()
    semesters = Semester.objects.all()
    context = {'program': program, 'courses': courses, 'semesters': semesters}
    return render(request, 'curriculum/curriculum.html', context)


def masters(request):
    program = Program.objects.get(program_name="Masters")
    courses = program.course_set.all()
    semesters = Semester.objects.all()
    context = {'program': program, 'courses': courses, 'semesters': semesters}
    return render(request, 'curriculum/curriculum.html', context)


def phd(request):
    program = Program.objects.get(program_name="Phd")
    courses = program.course_set.all()
    semesters = Semester.objects.all()
    context = {'program': program, 'courses': courses, 'semesters': semesters}
    return render(request, 'curriculum/curriculum.html', context)


def ccna(request):
    program = Program.objects.get(program_name="CCNA")
    courses = program.course_set.all()
    semesters = Semester.objects.all()
    context = {'program': program, 'courses': courses, 'semesters': semesters}
    return render(request, 'curriculum/curriculum.html', context)

