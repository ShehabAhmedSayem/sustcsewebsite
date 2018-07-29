from django.db import models

from people.models import ResearchArea, Faculty, Student


class ResearchGroup(models.Model):
    name = models.CharField(max_length=200)
    date_established = models.DateField()
    office = models.CharField(blank=True, null=True, max_length=500)
    research_area = models.ManyToManyField(ResearchArea, related_name="research_group")
    about = models.TextField(blank=True, null=True)
    rules = models.TextField(blank=True, null=True)
    site_link = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    contact = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name


class ResearchGroupFaculty(models.Model):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.faculty.name

    class Meta:
        verbose_name_plural = "research group faculties"


class ResearchGroupStudent(models.Model):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name


class ResearchGroupNotice(models.Model):
    title = models.CharField(max_length=500)
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)
    upload = models.FileField(blank=True, null=True, upload_to='research/notices/')

    def __str__(self):
        return self.title


class ResearchGroupResource(models.Model):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    purpose = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ResearchGroupProject(models.Model):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True)
    is_funded = models.BooleanField()
    amount = models.FloatField(blank=True, null=True)
    date_range = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PublicationType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=500)
    publication_type = models.ForeignKey(PublicationType, on_delete=models.CASCADE)
    published_year = models.CharField(max_length=10)
    link = models.URLField(blank=True, null=True)
    research_group = models.ForeignKey(ResearchGroup, blank=True, null=True, on_delete=models.SET_NULL)
    author_faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    author_student = models.ManyToManyField(Student, related_name="students")
    where_published = models.CharField(max_length=500)
    cited_by = models.IntegerField()

    def __str__(self):
        return self.title
