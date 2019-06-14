from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('project_management.urls')),
]
