from rest_framework import serializers

from resume.models import Employee, Skill, Education, Experience
from users.serializers import UserRegisterSerializer


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('company', 'start_year', 'end_year', 'work_type', 'location', 'description', 'employee')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('title', 'student_to', 'student_from', 'gpa', 'employee')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name',)


class EmployeeListSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'title', 'region', 'created_at', 'user')


class EmployeeSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    user = UserRegisterSerializer(read_only=True)
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id', 'title', 'region', 'birth_date', 'gender', 'user', 'experiences', 'education', 'skills', 'created_at',
            'updated_at')

    def get_skills(self, obj):
        return [skill.name for skill in obj.skills.all()]


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id', 'title', 'region', 'birth_date', 'gender', 'created_at',
            'updated_at')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        employee = super().create(validated_data)
        return employee

