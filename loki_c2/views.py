from django.shortcuts import render, get_object_or_404

from loki.models import Client, JobReport


def index(request):
    clients = Client.objects.all()
    return render(request, 'loki_c2/index.html', {'clients': clients})


def create_job(request):
    return render(request, 'loki_c2/create_job.html')


def job_history(request, uuid):
    client = get_object_or_404(Client, uuid=uuid)
    reports = JobReport.objects.filter(client=client).order_by('-job_id')
    return render(request, 'loki_c2/job_history.html', {'uuid': uuid, 'reports': reports})
