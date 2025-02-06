from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    productivity = models.FloatField()  
    skills = models.TextField()  
    years_of_experience = models.IntegerField()
    location = models.CharField(max_length=100)
    present_tasks = models.TextField()  
    present_project = models.CharField(max_length=100)
    nearest_deadline = models.DateField()
