from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404

def index(request):
    bugs_url = reverse('quality_control:bugs_list')
    features_url = reverse('quality_control:features_list')
    html = '<h1>Система контроля качества</h1>'
    html += '<ul>'
    html += f'<li><a href="{bugs_url}">Список всех багов</a></li>'
    html += f'<li><a href="{features_url}">Запросы на улучшение</a></li>'
    html += '</ul>'
    return HttpResponse(html)

def bugs_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Cписок отчетов об ошибках</h1>'
    bugs_html += '<ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

def features_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1>'
    features_html += '<ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h1>Детали бага {bug.id}</h1>'
    response_html += '<ul>'
    response_html += f'<li>Название: {bug.title}</li>'
    response_html += f'<li>Описание: {bug.description}</li>'
    response_html += f'<li>Статус: {bug.status}</li>'
    response_html += f'<li>Приоритет: {bug.priority}</li>'
    response_html += '</ul>'
    return HttpResponse(response_html)

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<h1>Детали улучшения {feature.id}</h1>'
    response_html += '<ul>'
    response_html += f'<li>Название: {feature.title}</li>'
    response_html += f'<li>Описание: {feature.description}</li>'
    response_html += f'<li>Статус: {feature.status}</li>'
    response_html += f'<li>Приоритет: {feature.priority}</li>'
    response_html += '</ul>'
    return HttpResponse(response_html)

# -------------------------------------------------------------------------

from django.views import View
from django.views.generic import ListView, DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_url = reverse('quality_control:bugs_list')
        features_url = reverse('quality_control:features_list')
        html = '<h1>Система контроля качества</h1>'
        html += '<ul>'
        html += f'<li><a href="{bugs_url}">Список всех багов</a></li>'
        html += f'<li><a href="{features_url}">Запросы на улучшение</a></li>'
        html += '</ul>'
        return HttpResponse(html)

class BugReportsListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Cписок отчетов об ошибках</h1>'
        bugs_html += '<ul>'
        for bug in bugs:
            bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)

class FeatureRequestsListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = '<h1>Список запросов на улучшение</h1>'
        features_html += '<ul>'
        for feature in features:
            features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
        features_html += '</ul>'
        return HttpResponse(features_html)

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = f'<h1>Детали бага {bug.id}</h1>'
        response_html += '<ul>'
        response_html += f'<li>Название: {bug.title}</li>'
        response_html += f'<li>Описание: {bug.description}</li>'
        response_html += f'<li>Статус: {bug.status}</li>'
        response_html += f'<li>Приоритет: {bug.priority}</li>'
        response_html += '</ul>'
        return HttpResponse(response_html)

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = f'<h1>Детали улучшения {feature.id}</h1>'
        response_html += '<ul>'
        response_html += f'<li>Название: {feature.title}</li>'
        response_html += f'<li>Описание: {feature.description}</li>'
        response_html += f'<li>Статус: {feature.status}</li>'
        response_html += f'<li>Приоритет: {feature.priority}</li>'
        response_html += '</ul>'
        return HttpResponse(response_html)
