# Generated by Django 2.0.5 on 2018-09-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0005_admissionform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissionform',
            name='program',
        ),
        migrations.AddField(
            model_name='program',
            name='admission_form',
            field=models.FileField(blank=True, null=True, upload_to='admission_form/'),
        ),
        migrations.DeleteModel(
            name='AdmissionForm',
        ),
    ]
