# Generated by Django 3.1 on 2022-06-08 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacher_elmi_meqalelerin_sayi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='elmi_meqalelerin_sayi',
        ),
    ]