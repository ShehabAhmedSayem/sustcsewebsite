from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, Http404
from .models import *
from .forms import *
from curriculum.models import Program
import os
from django.conf import settings


def admission_second_major(request):
    program = Program.objects.get(program_name="undergraduate_second_major")
    context = {'program': program}
    return render(request, 'admission/program-admission.html', context)


def admission_phd(request):
    program = Program.objects.get(program_name="phd")
    context = {'program': program}
    return render(request, 'admission/program-admission.html', context)


def admission_masters(request):
    program = Program.objects.get(program_name="masters")
    context = {'program': program}
    return render(request, 'admission/program-admission.html', context)


def admission_ccna(request):
    program = Program.objects.get(program_name="ccna")
    context = {'program': program}
    return render(request, 'admission/program-admission.html', context)

'''
def second_major_application(request):
    if request.method == 'GET':
        application_form = SecondMajorApplicationForm(request.GET or None)

    elif request.method == 'POST':
        application_form = SecondMajorApplicationForm(request.POST)

        if application_form.is_valid():
            application = application_form.save()
            return redirect('admission_second_major')

    return render(request, 'admission/second-major-application-form.html', {
        'application_form': application_form,
    })



def second_major_application(request):

    if request.method == 'GET':
        application_form = SecondMajorApplicationForm(request.GET or None)
        formset = SecondMajorCourseFormset(queryset=SecondMajorCourse.objects.none())

    elif request.method == 'POST':
        application_form = SecondMajorApplicationForm(request.POST)
        formset = SecondMajorCourseFormset(request.POST)

        if application_form.is_valid() and formset.is_valid():
            application = application_form.save()

            for form in formset:
                course = form.save(commit=False)
                course.registration = application
                course.save()
            return redirect('admission_second_major')

    context = {
        'application_form': application_form,
        'formset': formset,
    }
    return render(request, 'admission/second-major-application-form.html', context)
'''

def download_form(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404