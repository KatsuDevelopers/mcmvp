from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.

class PinModel(models.Model):
    pin_number = models.IntegerField(validators=[MaxLengthValidator(6)])
