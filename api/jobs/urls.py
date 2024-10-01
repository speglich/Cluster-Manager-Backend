from django.urls import path
from .views import (
    JobCreate,
    JobList,
    JobDetail,
)

urlpatterns = [
    path('', JobList.as_view(), name='list-jobs'),
    path('create/', JobCreate.as_view(), name='submit-job'),
    path('<int:pk>/', JobDetail.as_view(), name='job-detail'),
]
