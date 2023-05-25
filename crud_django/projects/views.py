from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.
'''
projectList = [

    {
        'id': '1',
        'title': 'e-commerce',
        'description': 'this is a full e-commerce'
    },
    {
        'id': '2',
        'title': 'portfolio',
        'description': 'this is a full portfolio'
    },
    {
        'id': '3',
        'title': 'social-network',
        'description': 'this is a full social-network'
    },
]
'''


def home(request):
    return HttpResponse("HOLA!!")


def projects(request):  # function for path('projects/',)
    # msg = 'PROJECTS PAGE',
    # num = 9,

    # context = {'number': num, 'message': msg, 'lists': projectList}
    project_list = Project.objects.all()
    context = {'lists': project_list}
    return render(request, 'projects/projects.html', context)
    # return render(request, 'projects/projects.html', {'MESSAGE': msg})
    # here, MESSAGE is KEY & msg is value


def project(request, pk):  # function for path('projects/',)
    """
    projectObj = None
    for values in projectList:
        if values['id'] == pk:
            projectObj = values
    """
    project_obj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    # inside_in {} 'site_tag': tags
    return render(request, 'projects/single-project.html', {'project': project_obj})


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

        # print(request.POST)  # print given value in terminal
        # print(request.POST['title'])  # print only title in terminal
    context = {'addnew_form': form}
    return render(request, 'projects/project_form.html', context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'addnew_form': form}
    return render(request, 'projects/project_form.html', context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_project.html', context)
