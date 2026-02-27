from django.db import models
from django.contrib.auth.models import User

class PredictionResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    sleep_hours = models.FloatField()
    study_hours = models.FloatField()
    meals_per_day = models.IntegerField()
    social_media_hours = models.FloatField()
    physical_activity_hours = models.FloatField()
    substance_use = models.CharField(max_length=10)
    academic_percentage = models.FloatField()
    predicted_category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_category}"