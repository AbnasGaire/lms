# Generated by Django 2.2.4 on 2019-09-29 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='is_firstlogin',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_suspend',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
