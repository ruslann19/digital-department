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

    # path('bugs/add_bug/', views.add_bug_report, name='add_bug_report'),
    # path('features/add_feature/', views.add_feature_request, name='add_feature_request'),
    # path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    # path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    # path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    # path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),

    path('bugs/add_bug/', views.BugReportCreateView.as_view(), name='add_bug_report'),
    path('features/add_feature/', views.FeatureRequestCreateView.as_view(), name='add_feature_request'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug'),
    path('features/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature'),
]
