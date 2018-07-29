import datetime

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from people.models import Faculty, Batch


class Program(models.Model):
    program_name = models.CharField(max_length=100)
    details = RichTextField()

    def __str__(self):
        return self.program_name


class Semester(models.Model):
    year_semester = models.CharField(max_length=10)

    def __str__(self):
        return self.year_semester


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
    year_semester = models.ForeignKey(Semester, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.course_title

    def getDept(self):
        return self.course_code[0:3]


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_teacher = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    is_current = models.BooleanField(default=False)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    year_semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.course_title

    class Meta:
        verbose_name_plural = "classes"
