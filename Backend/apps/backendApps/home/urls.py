from django.urls import path
from apps.backendApps.home.views import HomeView

app_name = "backend_home"

urlpatterns = [
    path(
        '', 
        HomeView.as_view(), 
        name='backend_home',
    ),
]