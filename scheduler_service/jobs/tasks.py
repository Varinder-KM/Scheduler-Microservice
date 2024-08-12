from celery import shared_task
from .models import Job
from datetime import datetime

@shared_task
def run_scheduled_jobs():
    jobs = Job.objects.filter(is_active=True)
    for job in jobs:
        # Dummy logic for job execution
        print(f"Executing {job.job_name}")
        job.last_run_timestamp = datetime.now()
        # Calculate the next run time based on the schedule_interval
        job.save()
