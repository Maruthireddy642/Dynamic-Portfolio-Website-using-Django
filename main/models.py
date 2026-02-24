from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # ✅ Added
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    branch = models.CharField(max_length=150)
    semester = models.CharField(max_length=50)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)  # ✅ Added

    def __str__(self):
        return self.name