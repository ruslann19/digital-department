from .models import Project, Task
from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, 'tasks/index.html')

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'projects_list': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project': project})

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

# -------------------------------------------------------------------------

from django.views import View
from django.views.generic import ListView, DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')

class ProjectsListView(ListView):
    model = Project
    context_object_name = 'projects_list'
    template_name = 'tasks/projects_list.html'

class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    context_object_name = 'project'
    template_name = 'tasks/project_detail.html'

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'
