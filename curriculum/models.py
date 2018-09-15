import datetime

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from people.models import Faculty, Batch


class Program(models.Model):
    PROGRAM_NAME = (
        ('undergraduate_major', 'Undergraduate Major'),
        ('undergraduate_second_major', 'Undergraduate Second Major'),
        ('masters', 'Masters'),
        ('phd', 'PhD'),
        ('ccna', 'CCNA'),
    )
    program_name = models.CharField(max_length=100, choices=PROGRAM_NAME)
    details = RichTextField()
    admission_form = models.FileField(blank=True, null=True, upload_to='admission_form/')

    def __str__(self):
        return self.get_program_name_display()


class Semester(models.Model):
    YEAR_SEMESTER = (
        ('1/1', '1st Year 1st Semester'),
        ('1/2', '1st Year 2nd Semester'),
        ('2/1', '2nd Year 1st Semester'),
        ('2/2', '2nd Year 2nd Semester'),
        ('3/1', '3rd Year 1st Semester'),
        ('3/2', '3rd Year 2nd Semester'),
        ('4/1', '4th Year 1st Semester'),
        ('4/2', '4th Year 2nd Semester'),
    )
    year_semester = models.CharField(max_length=10, choices=YEAR_SEMESTER)
    running = models.BooleanField(default=False)

    def __str__(self):
        return self.get_year_semester_display()


class Course(models.Model):
    COURSE_TYPES = (
        ('major', 'Major'),
        ('nonmajor', 'Non-Major'),
        ('elective', 'Elective'),
    )
    course_type = models.CharField(max_length=20, choices=COURSE_TYPES)
    course_code = models.CharField(max_length=20)
    course_title = models.CharField(max_length=100)
    course_details = models.TextField()
    course_credit = models.FloatField()
    program_name = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)
    year_semester = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.SET_NULL)
    currently_offering = models.BooleanField(default=True)

    def __str__(self):
        return self.course_title

    def getDept(self):
        return self.course_code[0:3]


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_teacher = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    is_current = models.BooleanField(default=False)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, default="1991")
    year_semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.course_title

    class Meta:
        verbose_name_plural = "classes"
