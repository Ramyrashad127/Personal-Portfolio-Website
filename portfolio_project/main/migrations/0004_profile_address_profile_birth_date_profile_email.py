# Generated by Django 5.1.1 on 2024-09-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_profile_bio_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
