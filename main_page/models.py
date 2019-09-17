from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.FilePathField(path="/Portfolio")
    github = models.CharField(max_length=200, default='https://github.com/rmiyahara')
    technology = models.CharField(max_length=20, default='None')
    description_short = models.CharField(max_length=200, default='None')
    date = models.CharField(max_length=100, default='None')
    description_long = models.TextField()

class Job(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    description4 = models.TextField()

class Skill(models.Model):
    language = models.CharField(max_length=100)