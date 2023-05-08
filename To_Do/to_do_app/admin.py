from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'details', 'date']