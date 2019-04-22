from django.db import models

class FeedbackData(models.Model):
    name=models.CharField(max_length=20)
    rating=models.IntegerField()
    time=models.DateTimeField()
    feedback=models.CharField(max_length=500)

# Create your models here.
