from django.forms import ModelForm
from . models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__' #show all the fields from class Project
        fields = ['title', 'description', 'demo_link',
                  'source_link', 'tags', ]
