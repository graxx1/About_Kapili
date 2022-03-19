from django.db import models

# Create your models here.
class Me(models.Model):
    name = models.CharField(max_length = 50, null=True, blank=True)
    course = models.CharField(max_length = 50, null=True, blank=True)
    year = models.CharField(max_length = 50, null=True, blank=True)

    def __str__(self):
        return self.name