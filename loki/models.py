from django.db import models


class Client(models.Model):
    uuid = models.UUIDField(primary_key=True)


class Job(models.Model):
    code = models.TextField()


class JobReport(models.Model):
    client_uuid = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    output = models.TextField()
