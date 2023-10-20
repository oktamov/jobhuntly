from django.urls import path

from vacancy.views import VacancyListView, VacancyDetailView, VacancyCreateView

urlpatterns = [
    path('list', VacancyListView.as_view(), name='vacancy-list'),
    path('<int:pk>', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('create', VacancyCreateView.as_view(), name='vacancy-create'),
]