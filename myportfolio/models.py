from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    profilePic = models.TextField(blank=True)
    skills = models.CharField(max_length=100, blank=True)

class education(models.Model):
    school = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

class experience(models.Model):
    duration = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    skills = models.CharField(max_length=100, blank=True)

class projects(models.Model):
    duration = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    associated_with = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    skills = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=100, blank=True)

class awards(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    issuedDate = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=100, blank=True)