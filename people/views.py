from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import *
from .forms import *
from .decorators import *


def faculty(request):
    faculties = Faculty.objects.all()
    context={'faculties': faculties}
    return render(request, 'people/faculty.html', context)


def faculty_detail(request, user_id):
    faculty = get_object_or_404(Faculty, pk=user_id)
    context={'faculty': faculty}
    return render(request, 'people/faculty-detail.html', context)


def student(request):
    context = {}
    return render(request, 'people/student.html', context)


def staff(request):
    context = {}
    return render(request, 'people/staff.html', context)


@login_required
@faculty_required
@transaction.atomic
def update_faculty(request):
    if request.method == 'POST':
        faculty_form = FacultyForm(request.POST, instance=request.user.faculty)

        if faculty_form.is_valid():
            faculty_form.save()
            return redirect('faculty_detail', request.user.id)
        else:
            pass

    else:
        faculty_form = FacultyForm(instance=request.user.faculty)

    return render(request, 'people/faculty-edit.html', {
        'faculty_form': faculty_form,
    })


@login_required
@faculty_required
@transaction.atomic
def add_education(request):
    if request.method == 'POST':
        education_form = EducationForm(request.POST, user=request.user)
        #education_form = EducationForm(request.POST, instance=request.user.faculty)

        if education_form.is_valid():
            education_form.save()
            return redirect('add_education')
        else:
            pass

    else:
        #education_form = EducationForm(instance=request.user.faculty)
        education_form = EducationForm(user=request.user)

    return render(request, 'people/faculty-add-education.html', {
        'education_form': education_form,
    })

@login_required
@faculty_required
@transaction.atomic
def add_experience(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        experience_form = FacultyForm(request.POST, instance=request.user.faculty)
        education_form = FacultyForm(request.POST, instance=request.user.faculty)
        social_profile_form = FacultyForm(request.POST, instance=request.user.faculty)
        faculty_form = FacultyForm(request.POST, instance=request.user.faculty)

        if user_form.is_valid() and faculty_form.is_valid() and experience_form.is_valid() \
                and education_form.is_valid() and social_profile_form.is_valid():
            user_form.save()
            faculty_form.save()
            experience_form.save()
            education_form.save()
            social_profile_form.save()
            return redirect('faculty_detail', request.user.id)
        else:
            pass

    else:
        user_form = UserForm(instance=request.user)
        faculty_form = FacultyForm(instance=request.user.faculty)
        experience_form = ExperienceForm(instance=request.user.faculty)
        education_form = EducationForm(instance=request.user.faculty)
        social_profile_form = SocialProfileForm(instance=request.user.faculty)

    return render(request, 'people/faculty-edit.html', {
        'user_form': user_form,
        'faculty_form': faculty_form,
        'experience_form': experience_form,
        'education_form': education_form,
        'social_profile_form': social_profile_form,
    })

