from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from curriculum.models import Program


def admission_second_major(request):
    program = Program.objects.get(program_name="Undergraduate Second Major")
    context = {'program': program}
    return render(request, 'admission/program-admission.html', context)


def admission_phd(request):
    program = Program.objects.get(program_name="Phd")
    context = {'program': program}
    return render(request, 'admission/program-admission.html', context)


def admission_masters(request):
    program = Program.objects.get(program_name="Masters")
    context = {'program': program}
    return render(request, 'admission/program-admission.html', context)


def admission_ccna(request):
    program = Program.objects.get(program_name="CCNA")
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
'''


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