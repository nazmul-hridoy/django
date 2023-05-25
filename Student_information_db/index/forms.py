from django import forms
from index import models

class StudentForm(forms.ModelForm):
    class Meta:
        model  = models.Students
        fields = "__all__"

