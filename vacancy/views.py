from rest_framework import generics, permissions

from custom_permission import IsOwnerOrReadOnly
from resume.models import Skill
from resume.serializers import SkillSerializer
from .models import Vacancy
from .serializers import VacancySerializer, VacancyListSerializer, VacancyCreateSerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes = [IsOwnerOrReadOnly]


class VacancyCreateView(generics.CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkillsAddToVacancyCreateView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        employee_id = self.kwargs.get('pk')
        employee = Vacancy.objects.get(id=employee_id)
        skill_name = serializer.validated_data.get('name')
        skill, created = Skill.objects.get_or_create(
            name=skill_name)
        employee.skills.add(skill)
