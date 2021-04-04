from django.contrib import admin
from .models import Student

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    List_display = ['id', 'name', 'roll', 'city']





