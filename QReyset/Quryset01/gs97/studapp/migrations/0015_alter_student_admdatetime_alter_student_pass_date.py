# Generated by Django 4.2.6 on 2023-10-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0014_alter_student_admdatetime_alter_student_pass_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admdatetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='pass_date',
            field=models.DateField(),
        ),
    ]
