from django.db import models

# Create your models here
American = 'American Indian/ Alaskan Native'
Asian = 'Asian'
Black = 'Black/African American'
Native = 'Native Hawiian/ Other Pacific Islander'
White = 'White'
Other = 'Other'
Races = (
	(American = 'American Indian/ Alaskan Native'),
	(Asian = 'Asian'),
	(Black = 'Black/African American'),
	(Native = 'Native Hawiian/ Other Pacific Islander'),
	(White = 'White'),
	(Other = 'Other'),
	)

class Register(models.Model):
	first = models.CharField(max_length=32)
	last = models.CharField(max_length=32)
	address = models.TextField(blank=True)
	telephone = models.IntegerField(max_length=12)
	is_homeless = models.BooleanField(default=False)
	ethnicity = models.CharField(max_length=5, choices=Races, default=American)