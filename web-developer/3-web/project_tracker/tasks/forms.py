from django.forms import ModelForm
from .models import Project, Task

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('description', css_class='form-control', rows=3),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('description', css_class='form-control', rows=3),
            Field('status', css_class='form-select'),
            Field('assignee', css_class='form-select'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
