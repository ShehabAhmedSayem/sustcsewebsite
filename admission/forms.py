from django import forms
from django.forms import modelformset_factory
from .models import *


class SecondMajorApplicationForm(forms.ModelForm):
    class Meta:
        model = SecondMajorApplication
        fields = '__all__'


SecondMajorCourseFormset = modelformset_factory(
    SecondMajorCourse,
    fields=('course_code', 'course_credit', 'course_grade', ),
    extra=1,
)