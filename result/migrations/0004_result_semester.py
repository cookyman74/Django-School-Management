# Generated by Django 2.2.7 on 2019-11-24 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20191125_0353'),
        ('result', '0003_auto_20191125_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Semester'),
        ),
    ]
