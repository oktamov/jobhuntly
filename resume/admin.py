from django.contrib import admin
from .models import Employee, Experience, Education, Skill


# Basic admin for Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'region', 'birth_date', 'gender')
    search_fields = ('user__email', 'title', 'region')


# Basic admin for Experience model
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'company', 'start_year', 'end_year', 'work_type', 'location')
    search_fields = ('employee__user__email', 'company')


# Basic admin for Education model
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'title', 'student_from', 'student_to', 'gpa')
    search_fields = ('employee__user__email', 'title')


# Basic admin for Skill model
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

