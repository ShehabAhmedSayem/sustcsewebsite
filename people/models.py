from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class ResearchArea(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='people/images/')
    office = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    socialLinks = ["Dribbble.png", "Facebook.png", "Github.png", "YouTube.png", "Twitter.png", "Pinterest.png",
                   "Linkedin.png", "Google+.png", "Snapchat.png", "Instagram.png"]

    class Meta:
        abstract = True


class Faculty(People):
    research_interest = models.ManyToManyField(ResearchArea, related_name="faculty")
    STATUS = (
        ('in_service', 'In service'),
        ('on_leave', 'On leave'),
        ('ex', 'Ex Faculty'),
    )
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "faculties"


class SocialProfile(models.Model):
    name = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return self.link


class Staff(People):
    STATUS = (
        ('in_service', 'In service'),
        ('ex', 'Ex Staff'),
    )
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.name


class Batch(models.Model):
    batch_year = models.IntegerField()

    def __str__(self):
        return str(self.batch_year)

    class Meta:
        verbose_name_plural = "batches"


class Student(models.Model):
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


class ResearchStudent(models.Model):
    faculty_name = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    research_area = models.ForeignKey(ResearchArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty_name + " -> " + self.student_name


class Award(models.Model):
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
    name = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    experience_type = models.CharField(max_length=20, choices=EXP_TYPE)
    organization = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    time_duration = models.CharField(max_length=100)

    def __str__(self):
        return self.experience_type


class Education(models.Model):
    name = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    passing_year = models.IntegerField()
    specialization = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.degree

