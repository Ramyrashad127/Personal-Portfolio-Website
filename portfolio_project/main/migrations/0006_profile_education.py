# Generated by Django 5.1.1 on 2024-09-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(default=''),
        ),
    ]
