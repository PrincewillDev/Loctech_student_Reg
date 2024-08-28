from django.db import models

# Create your models here.
# myapp/models.py

from django.db import models

# class StudentRegistration(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.CharField(max_length=255)
#     qualification = models.CharField(max_length=100)
#     next_of_kin = models.CharField(max_length=100)
#     course = models.CharField(max_length=100)
#     occupation = models.CharField(max_length=100)
#     hear_about_us = models.CharField(max_length=255)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     state_of_origin = models.CharField(max_length=50)
#     course_duration = models.CharField(max_length=50)
#     start_date = models.DateField()
#     instructor = models.CharField(max_length=100)
#     type_of_training = models.CharField(max_length=50)
#     payment_plan = models.CharField(max_length=50)
#     registering_officer = models.CharField(max_length=100)
#     date = models.DateField()

#     def __str__(self):
#         return self.name
