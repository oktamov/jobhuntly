from django.contrib import admin
from .models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'level', 'job_type', 'salary', 'user', 'created_at')
    list_filter = ('level', 'job_type', 'created_at')
    search_fields = ('title', 'company', 'description', 'user__username')
    raw_id_fields = ('user',)  # Use a search-enabled widget for user selection
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


admin.site.register(Vacancy, VacancyAdmin)
