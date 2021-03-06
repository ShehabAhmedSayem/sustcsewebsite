# Generated by Django 2.0.5 on 2018-08-11 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_auto_20180811_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publication_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='research.PublicationType'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='published_year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
