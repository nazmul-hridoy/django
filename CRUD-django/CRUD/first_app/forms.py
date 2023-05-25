from django import forms
from first_app import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student  # from_models.py _class
        fields = "__all__"
