# Generated by Django 5.1 on 2024-09-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_profile_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.TextField(),
        ),
    ]
