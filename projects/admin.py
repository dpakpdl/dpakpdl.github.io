from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technology']


admin.site.register(Project, ProjectAdmin)
