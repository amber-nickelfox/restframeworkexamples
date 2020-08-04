from django.db import models

# Create your models here.


class Company(models.Model):
    """This is company model"""

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """This is company Employee model"""

    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
