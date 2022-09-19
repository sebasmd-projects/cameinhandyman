from django.urls import path
from apps.backendApps.api_guide.views import ApiGuideView

app_name = "backend_api_guide"

urlpatterns = [
    path(
        '', 
        ApiGuideView.as_view(), 
        name='backend_api_guide',
    ),
]