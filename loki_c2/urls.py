from django.urls import path

from loki_c2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-job', views.create_job, name='create_job'),
    path('job-history/<str:uuid>', views.job_history, name='job_history'),
]