from django.urls import path

from . import views

urlpatterns = [
    path('register', views.Register.as_view()),
    path('jobs/create', views.create_job),
    path('jobs', views.list_jobs),
    path('jobs/<int:job_id>', views.get_job),
    path('jobs/<int:job_id>/report', views.report_job),
]
