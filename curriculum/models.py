import datetime

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Curriculum(models.Model):
    program_name = models.CharField(max_length=100)
    curriculum_details = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.program_name
