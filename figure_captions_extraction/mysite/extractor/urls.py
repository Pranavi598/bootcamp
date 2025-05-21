from django.urls import path
from . import views_dashboard

urlpatterns = [
    path('', views_dashboard.dashboard_view, name='dashboard'),
    path('submit/', views_dashboard.submit_ids, name='submit_ids'),
    path('download/csv/', views_dashboard.download_csv, name='download_csv'),
    path('download/json/', views_dashboard.download_json, name='download_json'),
]
