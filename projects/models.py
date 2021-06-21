from django.db import models

class project(models.Model):
    title = models.CharField(max_length=200)
    image = models.FilePathField(path="/img")
    technology = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title