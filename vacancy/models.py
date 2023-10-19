from django.db import models

from resume.models import Skill
from users.models import User


class Vacancy(models.Model):
    LEVEL_CHOICES = (
        ('Internship', 'Internship'),
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    )
    JOB_TYPE_CHOICES = (
        ('full time', 'full time'),
        ('part time', 'part time'),
    )
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='images/', blank=True, null=True)
    experience = models.CharField(max_length=255)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='Junior')
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default='full time')
    salary = models.IntegerField(default=0)
    overview = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    offer = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name="vacancies", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill, related_name="vacancies")

    def __str__(self):
        return self.title
