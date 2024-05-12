from django.db import models

class Banner(models.Model):
    body = models.CharField(max_length=255)
    banner_img = models.FileField(upload_to='banner/')


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    portfolio_img = models.FileField(upload_to='portfolio/')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    image = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    job_title = models.CharField(max_length=255)
    working_day = models.IntegerField()
    working_time = models.CharField(max_length=255, blank=True, null=True)
    requirements = models.TextField(blank=True)
    tasks = models.TextField(blank=True)
    technology = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.job_title + ' ' + self.salary


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cv = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.full_name
