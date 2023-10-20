from rest_framework import generics

from resume.models import Employee, Education, Experience, Skill
from resume.serializers import EmployeeSerializer, EmployeeListSerializer, EmployeeCreateSerializer, \
    EducationSerializer, ExperienceSerializer, SkillSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes =


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployeeEducationCreateView(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EmployeeExperienceCreateView(generics.CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class SkillsAddToEmployeeCreateView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def perform_create(self, serializer):
        employee_id = self.kwargs.get('pk')
        employee = Employee.objects.get(id=employee_id)
        skill_name = serializer.validated_data.get('name')
        skill, created = Skill.objects.get_or_create(
            name=skill_name)
        employee.skills.add(skill)
