from django.contrib import admin
from hackathon.forms import HackathonForm, ProjectForm
from hackathon.models import Hackathon, Project, UserProfile


class HackathonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'slogan', 'created', 'updated')
    form = HackathonForm


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abstract', 'members', 'created', 'updated')
    form = ProjectForm


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'manager', 'photo')

    def photo(self, obj):
        return '<img src="%s" style="height:100px" />' % obj.photo_url
    photo.allow_tags = True


admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(UserProfile, UserProfileAdmin)