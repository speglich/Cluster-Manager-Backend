# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters

from .models import Job
from .serializers import JobSerializer
import subprocess

class JobCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [OrderingFilter, SearchFilter, filters.DjangoFilterBackend]
    ordering_fields = ["submit_time", "start_time", "end_time"]
    search_fields = ["job_name"]
    filterset_fields = {
        "status": ["exact"],
        "submit_time": ["gte", "lte"],
        "start_time": ["gte", "lte"],
        "end_time": ["gte", "lte"],
    }

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class JobDetail(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer