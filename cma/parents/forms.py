from django import forms
from .models import Register , Household

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = 	('first','last','address','telephone','is_homeless','ethnicity',
	'gender','birthday','highschool_completed','disabled','school','community_area','ward')  


class HousingForm(forms.ModelForm):
	class Meta:
		model = Household
		fields = (
		'name',
		'family_type',
		'housing',
		'food_stamps',
		'free_lunch',
		'insurance',
		'employment',
		)


