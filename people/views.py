from django.shortcuts import render, get_object_or_404
from .models import *


def faculty(request):
    faculty = Faculty.objects.all()
    context={'faculty': faculty}
    return render(request, 'people/faculty.html', context)


def student(request):
    context={}
    return render(request, 'people/student.html', context)


def staff(request):
    context={}
    return render(request, 'people/staff.html', context)