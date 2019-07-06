from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
# Create your models here.
class GeoData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=False)
    CoordX = models.DecimalField(max_digits=8, decimal_places=6)
    CoordY = models.DecimalField(max_digits=8, decimal_places=6)