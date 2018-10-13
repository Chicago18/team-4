from django.db import models

# Create your models here.

class Parent(models.User):
    children = []
    governmentForm = ""
    familyIncomeForm = ""
    parentConsentForm = ""
    emergencyConsentForm = ""

class Child(models.User):
    grades = []

class Admin(models.User):
