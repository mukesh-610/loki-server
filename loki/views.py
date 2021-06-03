import base64
import binascii

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from loki.models import Client, Job, JobReport
from loki.serializers import ClientSerializer, JobSerializer, JobReportSerializer


class Register(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


@api_view(['POST'])
def create_job(request):
    try:
        code = base64.b64decode(request.data['code'])
    except (binascii.Error, KeyError):
        return Response('Invalid data', status=status.HTTP_400_BAD_REQUEST)
    if not code:
        return Response('Invalid data', status=status.HTTP_400_BAD_REQUEST)
    job = Job.objects.create(code=code)
    return Response({'job_id': job.id}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def list_jobs(request):
    try:
        client = get_object_or_404(Client, uuid=request.data['uuid'])
        previously_completed_jobs = JobReport.objects.filter(client=client).values_list('job_id', flat=True)
        jobs_to_do = Job.objects.exclude(id__in=previously_completed_jobs).values_list('id', flat=True)
    except KeyError:
        return Response('Invalid data', status=status.HTTP_400_BAD_REQUEST)
    return Response(jobs_to_do)


@api_view(['GET'])
def get_job(request, job_id):
    return Response(JobSerializer(get_object_or_404(Job, id=job_id)).data)


@api_view(['POST'])
def report_job(request, job_id):
    try:
        client = get_object_or_404(Client, uuid=request.data['uuid'])
        job = get_object_or_404(Job, id=job_id)
        output = request.data['output']
        report, created = JobReport.objects.get_or_create(client=client, job=job)
        if created:
            report.output = output
            report.save()
        serialized = JobReportSerializer(report)
    except KeyError:
        return Response('Invalid data', status=status.HTTP_400_BAD_REQUEST)
    return Response(serialized.data)
