from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    fields = '__all__'


admin.site.register(Project)
