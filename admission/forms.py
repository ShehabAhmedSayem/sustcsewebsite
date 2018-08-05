from django import forms
from django.forms import modelformset_factory
from .models import *


class SecondMajorApplicationForm(forms.ModelForm):
    class Meta:
        model = SecondMajorApplication
        fields = '__all__'


SecondMajorPreCourseListFormSet = modelformset_factory(
    SecondMajorPreCourseList,
    #exclude=('applicant',),
    fields='__all__',
    extra=1,
)
