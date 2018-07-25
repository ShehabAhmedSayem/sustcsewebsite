from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


def undergrad_major(request):
    program = Program.objects.get(program_name="Undergraduate Major")
    courses = program.course_set.all()
    semesters = Semester.objects.all()
    totalCreditPerSemester = {}
    totalCoursePerSemester = {}
    for semester in semesters:
        totalCredit = 0.0
        totalCourse = 0
        for course in courses:
            if str(course.year_semester) == str(semester.year_semester):
                totalCredit += course.course_credit
                totalCourse += 1
        totalCreditPerSemester[semester.year_semester] = totalCredit
        totalCoursePerSemester[semester.year_semester] = totalCourse
    context = {'program': program, 'courses': courses, 'semesters':semesters, 'totalCreditPerSemester':totalCreditPerSemester, 'totalCoursePerSemester':totalCoursePerSemester}
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

