# project_name/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import root_view  # Import the root_view function

urlpatterns = [
    path('', root_view, name='root'),  # Root path
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include your app's API routes
]
