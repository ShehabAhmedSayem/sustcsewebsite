# Generated by Django 2.0.5 on 2018-08-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admission', '0004_delete_secondmajorapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondMajorApplication',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('registration_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1000)),
                ('courses_taken', models.TextField(help_text='Write in the format : Course Code(space)Course Credit(space)Grade. Example: "EEE101 3.0 A+"')),
                ('incomplete_course', models.TextField(help_text='Write in the format : Course Code(space)Course Credit. Example: "EEE101 3.0"')),
                ('reason_of_study', models.TextField()),
            ],
        ),
    ]
