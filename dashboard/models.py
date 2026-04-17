
from django.db import models

class EmploymentData(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    province = models.CharField(max_length=50)

    employment = models.FloatField()
    unemployment_rate = models.FloatField()
    employment_rate = models.FloatField()
    participation_rate = models.FloatField()

    def __str__(self):
        return f"{self.province} - {self.year}"

