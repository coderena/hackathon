from django import forms
from hackathon.models import Hackathon, Project
from django_ace import AceWidget


class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        exclude = ('created', 'updated', 'slug')
        widgets = {
            'slogan': forms.Textarea(attrs={'style': 'width: 80%; height: 40px;'}),
            'instruction': AceWidget(mode='markdown'),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('created', 'updated')
        widgets = {
            'information': AceWidget(mode='markdown'),
            'members': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }