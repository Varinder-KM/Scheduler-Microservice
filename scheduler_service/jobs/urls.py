from django.urls import path
from .views import get_jobs, get_job_by_id, create_job

urlpatterns = [
    path('jobs/', get_jobs),
    path('jobs/<int:job_id>/', get_job_by_id),
    path('add_job/', create_job),
    path('', create_job)
]
