# Generated by Django 4.0.4 on 2022-05-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0003_alter_sessionyearmodel_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
