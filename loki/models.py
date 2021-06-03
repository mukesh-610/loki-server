from django.db import models


class Client(models.Model):
    uuid = models.UUIDField(primary_key=True)


class Job(models.Model):
    code = models.BinaryField()


class JobReport(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    output = models.TextField()
