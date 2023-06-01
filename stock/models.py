from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kospi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    total_price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class KospiHoldingUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kospi = models.ForeignKey(Kospi, on_delete=models.CASCADE)
    
