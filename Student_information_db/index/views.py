from django.shortcuts import render
from django.http import HttpResponse
from index.models import Students
#from index.forms import Student_form
from index import forms


# Create your views here.
def home(request):
    student_list = Students.objects.order_by('name')
    dictionary = {"Students": student_list}
    return render(request, 'index/index.html', context=dictionary)


def form(request):
    new_form = forms.StudentForm()
    if request.method == "POST":
        new_form = forms.StudentForm(request.POST)

    if new_form.is_valid():
        new_form.save(commit=True)
        return home(request)

    dictionary = {"test_form": new_form}
    return render(request, 'index/form.html', context=dictionary)
