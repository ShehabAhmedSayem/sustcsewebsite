from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', )


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['faculty'] = forms.ModelChoiceField(queryset=Faculty.objects.filter(user=user))


class SocialProfileForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = '__all__'