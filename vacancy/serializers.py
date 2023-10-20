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
    # skills = serializers.ListField(child=serializers.CharField(max_length=200))
    skills = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Skill.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Vacancy
        fields = (
            'id', 'title', 'company', 'company_logo', 'experience', 'level', 'job_type',
            'salary', 'overview', 'description', 'offer', 'skills', 'created_at'
        )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        skills_data = validated_data.pop('skills')
        vacancy = super().create(validated_data)
        skills = [Skill.objects.get_or_create(name=skill_name)[0] for skill_name in skills_data]
        vacancy.skills.add(*skills)

        return vacancy

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["skills"] = [skill.name for skill in instance.skills.all()]
        return data


