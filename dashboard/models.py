from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class PotentialLoss(models.Model):
    def __str__(self):
        return "{}".format(self.data_date)
    data_date = models.DateTimeField(default = timezone.now)
    Banking = models.FloatField(validators=[MinValueValidator(0)])
    Wholesale = models.FloatField(validators=[MinValueValidator(0)])
    Aggregation = models.FloatField(validators=[MinValueValidator(0)])
