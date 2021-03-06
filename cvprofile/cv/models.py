from django.db import models

# Create your models here.
# modeliu classe
class CvStructure(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    technology = models.CharField(max_length=200, blank=True)
    job_description = models.TextField()

    def __str__(self):
        return self.name

class Link(models.Model):
    link = models.TextField()
