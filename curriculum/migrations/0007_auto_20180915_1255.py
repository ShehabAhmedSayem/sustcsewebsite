# Generated by Django 2.0.5 on 2018-09-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0006_auto_20180912_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='currently_offering',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_name',
            field=models.CharField(choices=[('undergraduate_major', 'Undergraduate Major'), ('undergraduate_second_major', 'Undergraduate Second Major'), ('masters', 'Masters'), ('phd', 'P'), ('ccna', 'CCNA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='semester',
            name='year_semester',
            field=models.CharField(choices=[('1/1', '1st Year 1st Semester'), ('1/2', '1st Year 2nd Semester'), ('2/1', '2nd Year 1st Semester'), ('2/2', '2nd Year 2nd Semester'), ('3/1', '3rd Year 1st Semester'), ('3/2', '3rd Year 2nd Semester'), ('4/1', '4th Year 1st Semester'), ('4/2', '4th Year 2nd Semester')], max_length=10),
        ),
    ]
