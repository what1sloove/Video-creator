from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')
    create_time = models.DateTimeField(auto_now_add=True)
