from django.db import models


class Document(models.Model):
    md5 = models.CharField(max_length=40, blank=True, db_index=True)
    sha1 = models.CharField(max_length=50, blank=True, db_index=True)
    disk_size = models.BigIntegerField()
    content_type = models.CharField(max_length=100, blank=True)
    path = models.CharField(max_length=4000)
    filename = models.CharField(max_length=1000)
