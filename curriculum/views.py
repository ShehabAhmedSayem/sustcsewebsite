from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


def undergrad_major(request):
    return render(request, 'curriculum/curriculum.html', context={})

