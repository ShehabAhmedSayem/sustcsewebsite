from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class ResearchArea(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Batch(models.Model):
    batch_year = models.IntegerField()
    syllabus = models.FileField(blank=True, null=True, upload_to='syllabus/')

    def __str__(self):
        return str(self.batch_year)

    class Meta:
        verbose_name_plural = "batches"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_faculty = models.BooleanField(default=False)
    username = models.CharField(blank=True, null=True, max_length=150, default="N")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'is_faculty']

    def __str__(self):
        return self.email


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    about = models.CharField(blank=True, null=True, max_length=2000, default='Hi. A am a proud faculty of SUST CSE.')
    designation = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='people/images/')
    office = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, blank=True, null=True)
    research_interest = models.ManyToManyField(ResearchArea, related_name="faculty")

    STATUS = (
        ('in_service', 'In service'),
        ('on_leave', 'On leave'),
        ('ex', 'Ex Faculty'),
    )

    status = models.CharField(max_length=20, choices=STATUS)
    personal_website = models.URLField(blank=True, null=True)
    google_scholars_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def getFacultyStatus(self):
        if self.status == 'in_service':
            return "In service"
        elif self.status == 'on_leave':
            return "On leave"
        elif self.status == 'ex':
            return "Ex Faculty"

    class Meta:
        verbose_name_plural = "faculties"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    registration_no = models.CharField(max_length=12)
    STATUS = (
        ('current', 'Current'),
        ('allumni', 'Allumni'),
    )
    status = models.CharField(max_length=20, choices=STATUS)
    session = models.CharField(max_length=10)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SocialProfile(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return self.link


class ResearchStudent(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    research_area = models.ForeignKey(ResearchArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty.name + " -> " + self.student.name


class Award(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    details = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='awards/images/')

    def __str__(self):
        return self.title


class Experience(models.Model):
    EXP_TYPE = (
        ('academic', 'Academic'),
        ('technical', 'Technical'),
    )
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    experience_type = models.CharField(max_length=20, choices=EXP_TYPE)
    organization = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    time_duration = models.CharField(max_length=100)

    def __str__(self):
        return self.experience_type


class Education(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    passing_year = models.IntegerField()
    specialization = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.degree


class Staff(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='people/images/')
    office = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    STATUS = (
        ('in_service', 'In service'),
        ('ex', 'Ex Staff'),
    )
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.name
