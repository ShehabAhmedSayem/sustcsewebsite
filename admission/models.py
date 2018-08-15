from django.db import models


class SecondMajorApplication(models.Model):
    registration_no = models.CharField(max_length=12,primary_key=True)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    reason_of_study = models.TextField()

    def __str__(self):
        return self.registration_no


class SecondMajorCourse(models.Model):
    registration = models.ForeignKey(SecondMajorApplication, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=6)
    course_credit = models.FloatField()
    course_grade = models.CharField(max_length=2, default="F")

    def __str__(self):
        return self.course_code