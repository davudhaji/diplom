# Generated by Django 3.1 on 2022-06-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_meqale_meqaletipi'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='elmi_meqalelerin_sayi',
            field=models.IntegerField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
