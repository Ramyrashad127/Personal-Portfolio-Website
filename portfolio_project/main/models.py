from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    profile_pic = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg')
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(default="",null=True, blank=True)
    email = models.EmailField(default="",null=True, blank=True)
    phone = models.CharField(max_length=20, default="",null=True, blank=True)
    education = models.TextField(default="",null=True, blank=True)
    experience = models.TextField(default="",null=True, blank=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name
