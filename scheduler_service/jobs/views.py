from django.http import JsonResponse
from .models import Job
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

def get_jobs(request):
    jobs = Job.objects.all()
    jobs_list = list(jobs.values())
    return JsonResponse(jobs_list, safe=False)

def get_job_by_id(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        job_data = {
            'id': job.id,
            'job_name': job.job_name,
            'last_run_timestamp': job.last_run_timestamp,
            'next_run_timestamp': job.next_run_timestamp,
            'schedule_interval': job.schedule_interval,
            'is_active': job.is_active,
        }
        return JsonResponse(job_data)
    except Job.DoesNotExist:
        return JsonResponse({'error': 'Job not found'}, status=404)

def create_job(request):
    if request.method == 'GET':
        return render(request, 'Add_jobs.html')

    elif request.method == 'POST':
        job_name = request.POST.get('job_name')  # Correct way to access form data
        job_interval = request.POST.get('schedule_interval')  # Correct way to access form data

        # Create a new job and save it to the database
        job = Job.objects.create(
            job_name=job_name,
            schedule_interval=job_interval
        )

        # Return a JSON response with the job details
        return JsonResponse({'id': job.id, 'job_name': job.job_name}, status=201)