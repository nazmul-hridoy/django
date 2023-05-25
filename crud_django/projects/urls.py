from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    # declare projects(function) here,
    path('project/<str:pk>/', views.project, name="project"),
    # <str:pk> – this part is trickier. It means that Django expects a string value and will transfer it to a view
    # as a variable called pk.
    path('create-project/', views.create_project, name="create-project"),
    path('update-project/<str:pk>/', views.update_project, name="update-project"),
    path('delete-project/<str:pk>/', views.delete_project, name="delete-project"),

]
