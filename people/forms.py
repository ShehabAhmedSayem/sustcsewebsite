from django import forms
from .models import *
from research.models import Publication, PublicationType


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        exclude = ('user',)


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['faculty'] = forms.ModelChoiceField(queryset=Faculty.objects.filter(user=user), initial=0)


class ExperienceEditForm(forms.ModelForm):
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
        self.fields['faculty'] = forms.ModelChoiceField(queryset=Faculty.objects.filter(user=user), initial=0)


class EducationEditForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(PublicationForm, self).__init__(*args, **kwargs)
        self.fields['author_faculty'] = forms.ModelChoiceField(queryset=Faculty.objects.filter(user=user), initial=0)
        self.fields['author_student'] = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
        self.fields['publication_type'] = forms.ModelChoiceField(queryset=PublicationType.objects.all())


class PublicationEditForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'


class ResearchInterestForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'


class SocialProfileForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(SocialProfileForm, self).__init__(*args, **kwargs)
        self.fields['faculty'] = forms.ModelChoiceField(queryset=Faculty.objects.filter(user=user), initial=0)


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(AwardForm, self).__init__(*args, **kwargs)
        self.fields['faculty'] = forms.ModelChoiceField(queryset=Faculty.objects.filter(user=user), initial=0)


class AwardEditForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'