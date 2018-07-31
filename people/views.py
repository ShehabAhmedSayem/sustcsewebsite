from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import *
from .forms import *
from .decorators import *
from research.models import Publication


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
        faculty_form = FacultyForm(request.POST, request.FILES, instance=request.user.faculty)

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

        if education_form.is_valid():
            education_form.save()
            return redirect('add_education')
        else:
            pass

    else:
        education_form = EducationForm(user=request.user)

    return render(request, 'people/faculty-add-education.html', {
        'education_form': education_form,
    })


@login_required
@faculty_required
@transaction.atomic
def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.user.faculty == education.faculty:
        education.delete()
        messages.success(request, 'Successfully deleted!')
    else:
        messages.error(request, 'You don\'t have authorization!')

    return redirect('faculty_detail', request.user.id)


@login_required
@faculty_required
@transaction.atomic
def add_experience(request):
    if request.method == 'POST':
        experience_form = ExperienceForm(request.POST, user=request.user)

        if experience_form.is_valid():
            experience_form.save()
            return redirect('add_experience')
        else:
            pass

    else:
        experience_form = ExperienceForm(user=request.user)

    return render(request, 'people/faculty-add-experience.html', {
        'experience_form': experience_form,
    })


@login_required
@faculty_required
@transaction.atomic
def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.user.faculty == experience.faculty:
        experience.delete()
        messages.success(request, 'Successfully deleted!')
    else:
        messages.error(request, 'You don\'t have authorization!')

    return redirect('faculty_detail', request.user.id)


@login_required
@faculty_required
@transaction.atomic
def add_publication(request):
    if request.method == 'POST':
        publication_form = PublicationForm(request.POST, user=request.user)

        if publication_form.is_valid():
            publication_form.save()
            return redirect('add_publication')
        else:
            pass

    else:
        publication_form = PublicationForm(user=request.user)

    return render(request, 'people/faculty-add-publication.html', {
        'publication_form': publication_form,
    })


@login_required
@faculty_required
@transaction.atomic
def delete_publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    if request.user.faculty == publication.author_faculty:
        publication.delete()
        messages.success(request, 'Successfully deleted!')
    else:
        messages.error(request, 'You don\'t have authorization!')

    return redirect('faculty_detail', request.user.id)


@login_required
@faculty_required
@transaction.atomic
def add_social_profile(request):
    if request.method == 'POST':
        social_profile_form = SocialProfileForm(request.POST, user=request.user)

        if social_profile_form.is_valid():
            social_profile_form.save()
            return redirect('add_social_profile')
        else:
            pass

    else:
        social_profile_form = SocialProfileForm(user=request.user)

    return render(request, 'people/faculty-add-social-profile.html', {
        'social_profile_form': social_profile_form,
    })


@login_required
@faculty_required
@transaction.atomic
def delete_publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    if request.user.faculty == publication.author_faculty:
        publication.delete()
        messages.success(request, 'Successfully deleted!')
    else:
        messages.error(request, 'You don\'t have authorization!')

    return redirect('faculty_detail', request.user.id)


@login_required
@faculty_required
@transaction.atomic
def add_award(request):
    if request.method == 'POST':
        award_form = AwardForm(request.POST, request.FILES, user=request.user)

        if award_form.is_valid():
            award_form.save()
            return redirect('add_award')
        else:
            pass

    else:
        award_form = AwardForm(user=request.user)

    return render(request, 'people/faculty-add-award.html', {
        'award_form': award_form,
    })


@login_required
@faculty_required
@transaction.atomic
def delete_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    if request.user.faculty == award.faculty:
        award.delete()
        messages.success(request, 'Successfully deleted!')
    else:
        messages.error(request, 'You don\'t have authorization!')

    return redirect('faculty_detail', request.user.id)