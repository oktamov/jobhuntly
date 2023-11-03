from django.db import models

from users.models import User


class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'

    title = models.CharField(max_length=255)
    region = models.CharField(max_length=256, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=50, choices=Gender.choices, default=Gender.MALE)
    skills = models.ManyToManyField(Skill, related_name="employees")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employees")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class Experience(models.Model):
    class Type(models.TextChoices):
        Part = "part_time"
        Full = "full_time"
        Hybrid = "hybrid"

    class Location(models.TextChoices):
        Remote = "remote"
        On_site = "on site"
        Hybrid = "hybrid"

    employee = models.ForeignKey(Employee, related_name="experiences", on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    start_year = models.CharField(max_length=255)
    end_year = models.CharField(max_length=255)
    work_type = models.CharField(max_length=100, choices=Type.choices, default=Type.Full)
    location = models.CharField(max_length=100, choices=Location.choices, default=Location.On_site)
    description = models.CharField(max_length=255)


class Education(models.Model):
    title = models.CharField(max_length=255)
    student_to = models.DateField()
    student_from = models.DateField()
    gpa = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='education')



