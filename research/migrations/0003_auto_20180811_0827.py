# Generated by Django 2.0.5 on 2018-08-11 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0002_auto_20180811_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author_student',
            field=models.ManyToManyField(blank=True, related_name='students', to='people.Student'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_type',
            field=models.ForeignKey(default='Conference', on_delete=django.db.models.deletion.CASCADE, to='research.PublicationType'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='where_published',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
