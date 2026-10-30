from django.db import models


# Create your models here.
class product(models.Model):
    ProId=models.IntegerField(primary_key=True)
    ProName=models.CharField(max_length=30)
    ProPrice=models.IntegerField()

# class customer(models.Model):
    # CusId=models.IntegerField(primary_key=True)
    # CusName=models.CharField(max_length=30)
    # CusPrice=models.IntegerField()
    



