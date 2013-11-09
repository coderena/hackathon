from django.contrib import admin
from hackathon.forms import HackathonForm, ProjectForm
from hackathon.models import Hackathon, Project


class HackathonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'slogan', 'created', 'updated')
    form = HackathonForm

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abstract', 'members', 'created', 'updated')
    form = ProjectForm


admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(Project, ProjectAdmin)