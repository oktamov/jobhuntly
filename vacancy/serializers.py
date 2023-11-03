from rest_framework import serializers

from users.serializers import UserRegisterSerializer
from .models import Vacancy, Skill


class SkillNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name',)


class VacancySerializer(serializers.ModelSerializer):
    skills = SkillNameSerializer(many=True, read_only=True)
    user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'company', 'company_logo', 'experience', 'level', 'job_type',
            'salary', 'overview', 'description', 'offer', 'user', 'created_at', 'skills'
        )


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'company', 'company_logo', 'level', 'job_type',
            'salary', 'created_at'
        )


class VacancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'company', 'experience', 'level', 'job_type',
            'salary', 'overview', 'description', 'offer',
        )

