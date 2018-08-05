from django.db import models


class SecondMajorApplication(models.Model):
    name = models.CharField(max_length=200)
    registration_no = models.CharField(max_length=12,primary_key=True)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    reason_of_study = models.TextField()

    def __str__(self):
        return self.name


class SecondMajorPreCourseList(models.Model):
    applicant = models.ForeignKey(SecondMajorApplication, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=10)
    is_complete = models.BooleanField(default=False)
    grade = models.CharField(max_length=2)
    course_credit = models.FloatField()

    def __str__(self):
        return str(self.applicant.name) + " -> " + self.course_code
