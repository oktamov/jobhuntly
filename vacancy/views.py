from rest_framework import generics

from .models import Vacancy
from .serializers import VacancySerializer, VacancyListSerializer, VacancyCreateSerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes =


class VacancyCreateView(generics.CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
