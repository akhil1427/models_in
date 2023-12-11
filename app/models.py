from django.db import models

# Create your models here.
class county(models.Model):
    C_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.C_name

class capital(models.Model):
    county_name=models.OneToOneField(county,on_delete=models.CASCADE,default=True)
    capital_name=models.CharField(max_length=20)
    def __str__(self):
        return self.capital_name

