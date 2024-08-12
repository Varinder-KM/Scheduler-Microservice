from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    last_run_timestamp = models.DateTimeField(null=True, blank=True)
    next_run_timestamp = models.DateTimeField(null=True, blank=True)
    schedule_interval = models.CharField(max_length=255)  # e.g., 'daily', 'weekly', 'monthly'
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.job_name
