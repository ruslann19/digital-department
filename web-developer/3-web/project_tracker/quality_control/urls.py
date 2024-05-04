from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('bugs/', views.bugs_list, name='bugs_list'),
    # path('features/', views.features_list, name='features_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugReportsListView.as_view(), name='bugs_list'),
    path('features/', views.FeatureRequestsListView.as_view(), name='features_list'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
]
