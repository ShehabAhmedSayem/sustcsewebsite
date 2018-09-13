from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from curriculum.models import Program
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def account_redirect(request):
    return redirect('faculty_detail', request.user.id)


def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'num_visits': num_visits}
    return render(request, 'home/index.html', context)


def about(request):
    context = {}
    return render(request, 'home/about.html', context)


def contact(request):
    context = {}
    return render(request, 'home/contact.html', context)

def developer(request):
    context = {}
    return render(request, 'home/developer.html', context)


def undergrad_major(request):
    program = Program.objects.get(program_name="Undergraduate Major")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def undergrad_second_major(request):
    program = Program.objects.get(program_name="Undergraduate Second Major")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def masters(request):
    program = Program.objects.get(program_name="Masters")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def phd(request):
    program = Program.objects.get(program_name="Phd")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def ccna(request):
    program = Program.objects.get(program_name="CCNA")
    context = {'program': program}
    return render(request, 'home/program_details.html', context)


def publications(request):
    context = {}
    return render(request, 'home/publications.html', context)
