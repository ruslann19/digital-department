from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, 'quality_control/index.html')

def bugs_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bugs})

def features_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features_list': features})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

# -------------------------------------------------------------------------

from django.views import View
from django.views.generic import ListView, DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

class BugReportsListView(ListView):
    model = BugReport
    context_object_name = 'bugs_list'
    template_name = 'quality_control/bugs_list.html'

class FeatureRequestsListView(ListView):
    model = FeatureRequest
    context_object_name = 'features_list'
    template_name = 'quality_control/features_list.html'

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    template_name = 'quality_control/bug_detail.html'

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    template_name = 'quality_control/feature_detail.html'

# -------------------------------------------------------------------------

from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm

def add_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})

def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bugs_list')

def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:features_list')

# -------------------------------------------------------------------------

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs_list')

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features_list')

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    context_object_name = 'bug'
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs={'bug_id': self.object.id})

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    context_object_name = 'feature'
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs={'feature_id': self.object.id})

class BugReportDeleteView(DeleteView):
    model = BugReport
    context_object_name = 'bug'
    template_name = 'quality_control/bug_confirm_delete.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs_list')

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    context_object_name = 'feature'
    template_name = 'quality_control/feature_confirm_delete.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features_list')
