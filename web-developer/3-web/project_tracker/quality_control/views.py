from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bugs_url = reverse('quality_control:bug_list')
    features_url = reverse('quality_control:feature_list')
    html = f'''
        <h1>Система контроля качества</h1>
        <a href='{bugs_url}'>Список всех багов</a><br>
        <a href='{features_url}'>Запросы на улучшение</a></br>
    '''
    return HttpResponse(html)

def bug_list(request):
    bugs_html = '<h1>Cписок отчетов об ошибках</h1>'
    return HttpResponse(bugs_html)

def feature_list(request):
    features_html = '<h1>Список запросов на улучшение</h1>'
    return HttpResponse(features_html)

def bug_detail(request, bug_id):
    response_html = f'<h1>Детали бага {bug_id}</h1>'
    return HttpResponse(response_html)

def feature_detail(request, feature_id):
    response_html = f'<h1>Детали улучшения {feature_id}</h1>'
    return HttpResponse(response_html)
