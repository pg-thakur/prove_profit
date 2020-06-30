from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.

class detail(models.Model):
    entity=models.CharField(max_length=50)
    industry=models.CharField(max_length=50)
    period1=models.IntegerField()
    period2=models.IntegerField()

class bss_set1(models.Model):
    total_non_current_asset=models.DecimalField( max_digits=15, decimal_places=3)
    total_current_asset=models.DecimalField( max_digits=15, decimal_places=3) 
    inventories=models.DecimalField( max_digits=15, decimal_places=3)
    trade_other_current=models.DecimalField( max_digits=15, decimal_places=3)
    cash=models.DecimalField( max_digits=15, decimal_places=3)
    issued_capital=models.DecimalField( max_digits=15, decimal_places=3)
    eqity=models.DecimalField( max_digits=15, decimal_places=3)
    non_current_liability=models.DecimalField( max_digits=15, decimal_places=3)
    current_liability=models.DecimalField( max_digits=15, decimal_places=3)
    intangible_asset=models.DecimalField( max_digits=15, decimal_places=3,null=True)
