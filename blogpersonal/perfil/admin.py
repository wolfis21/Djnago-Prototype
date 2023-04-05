from django.contrib import admin

#models
from .models import Project
# Register your models here.

@admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'desc', 'created')
    list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')