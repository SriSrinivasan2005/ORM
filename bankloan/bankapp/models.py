from django.db import models
from django.contrib import admin
class bankloan(models.Model):
    cust_name=models.CharField( max_length=50,primary_key=True)
    loan_ID=models.IntegerField()
    loan_type=models.CharField(max_length=50)
    loan_amnt=models.FloatField()
    cust_acno=models.IntegerField()
           
# Create your models here.
class bankloanAdmin(admin.ModelAdmin):
           list_display = ('cust_name','loan_ID','loan_type','loan_amnt','cust_acno')
           