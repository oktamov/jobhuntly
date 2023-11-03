from django.urls import path

from vacancy.views import VacancyListView, VacancyDetailView, VacancyCreateView, SkillsAddToVacancyCreateView

urlpatterns = [
    path('list', VacancyListView.as_view(), name='vacancy-list'),
    path('<int:pk>', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('create', VacancyCreateView.as_view(), name='vacancy-create'),
    path('<int:pk>/skills', SkillsAddToVacancyCreateView.as_view(), name='skills-create'),

]