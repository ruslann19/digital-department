from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='tasks/')),
    path('tasks/', include('tasks.urls')),
    path('quality_control/', include('quality_control.urls')),
]
