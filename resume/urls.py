from django.urls import path

from resume.views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeEducationCreateView, \
    EmployeeExperienceCreateView, SkillsAddToEmployeeCreateView

urlpatterns = [
    path('list', EmployeeListView.as_view(), name='Employee-list'),
    path('<int:pk>', EmployeeDetailView.as_view(), name='Employee-detail'),
    path('create', EmployeeCreateView.as_view(), name='Employee-create'),
    path('educations/create', EmployeeEducationCreateView.as_view(), name='educations-create'),
    path('experience/create', EmployeeExperienceCreateView.as_view(), name='experience-create'),
    path('<int:pk>/skills', SkillsAddToEmployeeCreateView.as_view(), name='skills-create'),
]
