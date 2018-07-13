from django.shortcuts import render, get_object_or_404
from .models import *


def faculty(request):
    faculties = Faculty.objects.all()
    context={'faculties': faculties}
    return render(request, 'people/faculty.html', context)


def faculty_detail(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    context={'faculty': faculty}
    return render(request, 'people/faculty-detail.html', context)


def student(request):
    context={}
    return render(request, 'people/student.html', context)


def staff(request):
    context={}
    return render(request, 'people/staff.html', context)