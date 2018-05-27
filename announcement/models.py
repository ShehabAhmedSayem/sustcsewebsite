from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class ProgramCategory(models.Model):
    program_name = models.CharField(max_length=100)

    def __str__(self):
        return self.program_name


class Notice(models.Model):
    program_year = models.ForeignKey(ProgramCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    date_published = models.DateField(auto_now_add=True)
    upload = models.FileField(upload_to='notices/%Y/%m/%d/')

    def __str__(self):
        return self.title

