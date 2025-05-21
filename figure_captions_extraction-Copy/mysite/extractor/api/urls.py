from django.urls import path
from .views import submit_ids, get_paper_data, health

urlpatterns = [
    path("submit_ids/", submit_ids),
    path("get_data/", get_paper_data),
    path("health/", health),
]
