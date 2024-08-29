from django.contrib import admin
from .models import Mentor, Project, Group, Student

# Register your models here.


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ["mentor", "mid"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["project_id", "project_title"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["group_id", "project_id", "mid"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["student", "usn", "group_id"]
