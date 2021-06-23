from django.db import models

class about_person(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    programming_languages = models.CharField(max_length=100)
    create_on = models.DateTimeField(auto_now_add=True)