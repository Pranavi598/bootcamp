# from django.urls import path
# from .views_dashboard import (
#     dashboard_view, submit_ids, download_csv, download_json
# )
#
# urlpatterns = [
#     path('dashboard/', dashboard_view, name='dashboard'),
#     path('submit/', submit_ids, name='submit_ids'),
#     path('download/csv/', download_csv, name='download_csv'),
#     path('download/json/', download_json, name='download_json'),
# ]
from django.urls import path
from . import views_dashboard

urlpatterns = [
    path('', views_dashboard.dashboard_view, name='dashboard'),
    path('submit/', views_dashboard.submit_ids, name='submit_ids'),
    path('download/csv/', views_dashboard.download_csv, name='download_csv'),
    path('download/json/', views_dashboard.download_json, name='download_json'),
]
