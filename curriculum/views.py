from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from .models import *
from people.models import Batch
import os
from django.conf import settings


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


def undergrad_second_major(request):
    program = Program.objects.get(program_name="Undergraduate Second Major")
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
    context = {'program': program, 'courses': courses, 'semesters': semesters,
               'totalCreditPerSemester': totalCreditPerSemester, 'totalCoursePerSemester': totalCoursePerSemester}
    return render(request, 'curriculum/curriculum.html', context)


def masters(request):
    program = Program.objects.get(program_name="Masters")
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
    context = {'program': program, 'courses': courses, 'semesters': semesters,
               'totalCreditPerSemester': totalCreditPerSemester, 'totalCoursePerSemester': totalCoursePerSemester}
    return render(request, 'curriculum/curriculum.html', context)


def phd(request):
    program = Program.objects.get(program_name="Phd")
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
    context = {'program': program, 'courses': courses, 'semesters': semesters,
               'totalCreditPerSemester': totalCreditPerSemester, 'totalCoursePerSemester': totalCoursePerSemester}
    return render(request, 'curriculum/curriculum.html', context)


def ccna(request):
    program = Program.objects.get(program_name="CCNA")
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
    context = {'program': program, 'courses': courses, 'semesters': semesters,
               'totalCreditPerSemester': totalCreditPerSemester, 'totalCoursePerSemester': totalCoursePerSemester}
    return render(request, 'curriculum/curriculum.html', context)


def syllabus(request):
    batches = Batch.objects.all()
    context = {'batches':batches}
    return render(request, 'curriculum/syllabus.html', context)


def download_syllabus(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404

