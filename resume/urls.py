from django.urls import path

from resume.views import EmployeeListView, EmployeeDetailView

urlpatterns = [
    path('list', EmployeeListView.as_view(), name='Employee-list'),
    path('<int:pk>', EmployeeDetailView.as_view(), name='Employee-detail'),
]