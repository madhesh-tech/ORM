from django.db import models
from django.contrib import admin
class Employee(models.Model):
    User_name=models.CharField(max_length=100)
    email=models.EmailField()
    Phone_Number=models.IntegerField()
    MovieName=models.CharField(max_length=100)
    seats=models.IntegerField()
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('User_name','email','Phone_Number','MovieName','seats')