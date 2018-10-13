from django.db import models

# Create your models here
American = 'American Indian/ Alaskan Native'
Asian = 'Asian'
Black = 'Black/African American'
Native = 'Native Hawiian/ Other Pacific Islander'
White = 'White'
Other = 'Other'
Races = (
	(American , 'American Indian/ Alaskan Native'),
	(Asian , 'Asian'),
	(Black , 'Black/African American'),
	(Native , 'Native Hawiian/ Other Pacific Islander'),
	(White , 'White'),
	(Other , 'Other'),
	)
male = 'Male'
female = 'Female'
gender = (
	(male ,'Male'),
	(female, 'Female')

	)
class Register(models.Model):
	first = models.CharField(max_length=32)
	last = models.CharField(max_length=32)
	address = models.CharField(max_length=128)
	telephone = models.IntegerField()
	is_homeless = models.BooleanField(default=False)
	ethnicity = models.CharField(max_length=32, choices=Races, default=American)
	gender = models.CharField(max_length=10, choices=gender, default=male)
	birthday = models.DateField(default=False)
	highschool_completed = models.CharField(blank=True,max_length=128)
	disabled = models.BooleanField(default=True)
	school = models.CharField(blank=True,max_length=128)
	community_area = models.CharField(blank=True ,max_length=256)
	ward = models.CharField(blank=True,max_length=256)

	def __str__(self):
		return f"{self.id}-{self.first.upper()} - {self.last.upper()}"


# Family Choices
single = 'Single Parent/Male'
single_f = 'Single Parent/Female'
two_parent = 'Two Parent'
ind_youth = 'Independant Youth'
relative = 'Relative'
guardian = 'Guardian'


family = (
(single , 'Single Parent/Male'),
(single_f , 'Single Parent/Female'),
(two_parent , 'Two Parent'),
(ind_youth , 'Independant Youth'),
(relative , 'Relative'),
(guardian , 'Guardian'),

)

rent = 'Rent'
own = 'Own'
homeless = 'Homeless/Shelter'
temp = 'In Temporary Housing'

house = (
(rent , 'Rent'),
(own , 'Own'),
(homeless , 'Homeless/Shelter'),
(temp , 'In Temporary Housing'),

)

employ = 'Employment'
pension = 'Pension'
tanf = 'TANF'
earnfare = 'EARNFARE'
ssn = 'Social Security'
unemploy = 'Unemployment Insurance'
other = 'Including SSDI,Child Support and VA Benefits'
ssi = 'SSI'

jobs = (
(employ, 'Employment'),
(pension, 'Pension'),
(tanf, 'TANF'),
(earnfare, 'EARNFARE'),
(ssn, 'Social Security'),
(unemploy, 'Unemployment Insurance'),
(other ,'Including SSDI,Child Support and VA Benefits'),
(ssi ,'SSI')
)

class Household(models.Model):
	name = models.ForeignKey(Register,on_delete=models.CASCADE , related_name="first_name")
	family_type = models.CharField(max_length=25, choices=family, default=single)
	housing = models.CharField(max_length=32, choices=house, default=rent)
	food_stamps = models.BooleanField(default=True)
	free_lunch = models.BooleanField(default=True)
	insurance = models.BooleanField(default=True)
	employment = models.CharField(max_length=45, choices=jobs, default=pension)
	
	def __str__(self):
		return f"{self.id}-{self.name} - {self.gender}"

# class Children(models.Model):
# 	parent = ForeignKey(Register, on_delete=models.CASCADE, related_name="parent_name")
# 	first_name = models.CharField(max_length=64)
# 	last_name = models.CharField(max_length=64)