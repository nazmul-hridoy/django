from django.shortcuts import render
from first_app import forms
from first_app.models import Student


# Create your views here.

def index(request):
    student_list = Student.objects.order_by('first_name')
    dictionary = {'title': "Index", 'student_list': student_list}
    return render(request, 'first_app/index.html', context=dictionary)


def student_form(request):
    form = forms.StudentForm  # from_forms.py_class

    if request.method == "POST":
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    dictionary = {'title': "Student Form", 'student_form': form}  # form_shows_in_student_form
    return render(request, 'first_app/student_form.html', context=dictionary)


def student_info(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    dictionary = {'student_info': student_info}
    return render(request, 'first_app/student_info.html', context=dictionary)


def student_update(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    form = forms.StudentForm(instance=student_info)  # for update student info

    if request.method == "POST":
        form = forms.StudentForm(request.POST, instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    dictionary = {'student_form': form}
    return render(request, 'first_app/student_update.html', context=dictionary)


def student_delete(request, student_id):
    student = Student.objects.get(pk=student_id).delete()
    dictionary = {'delete_message': "Successfully Delete"}
    return render(request, 'first_app/student_delete.html', context=dictionary)
