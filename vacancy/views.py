from rest_framework import generics

from .models import Vacancy
from .serializers import VacancySerializer, VacancyListSerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes =
