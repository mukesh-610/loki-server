from rest_framework import serializers

from loki.models import Client, Job, JobReport


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['uuid']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'code']


class JobReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobReport
        fields = ['id', 'client', 'job', 'output']
