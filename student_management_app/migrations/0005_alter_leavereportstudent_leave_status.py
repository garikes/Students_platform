# Generated by Django 4.0.4 on 2022-05-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0004_alter_attendance_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]