from django.forms import ModelForm
from .models import BugReport, FeatureRequest

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('description', css_class='form-control', rows=3),
            Field('project', css_class='form-select'),
            Field('task', css_class='form-select'),
            Field('status', css_class='form-select'),
            Field('priority', css_class='form-select'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )

class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('description', css_class='form-control', rows=3),
            Field('project', css_class='form-select'),
            Field('task', css_class='form-select'),
            Field('status', css_class='form-select'),
            Field('priority', css_class='form-select'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
