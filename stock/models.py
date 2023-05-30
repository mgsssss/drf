from django.db import models

# Create your models here.

class Kospi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    total_price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name