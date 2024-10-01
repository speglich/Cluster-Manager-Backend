from django.db import models

class Job(models.Model):
    job_id = models.IntegerField(unique=True)
    job_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    submit_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    output = models.CharField(max_length=255, null=True, blank=True)
    error = models.CharField(max_length=255, null=True, blank=True)