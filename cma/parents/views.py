from django.shortcuts import render , redirect
from . forms import RegisterForm , HousingForm
# Create your views here.
# This function is rendering index page
def index(request):
	return render(request,'parents/index.html')

def form(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('/form-2',pk=post.pk)
	else:
		form=RegisterForm()
	return render(request, 'parents/forms.html',{'form':form})

def housing(request):
	if request.method == "POST":
		form = HousingForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('/',pk=post.pk)
	else:
		form=HousingForm()
	return render(request, 'parents/form_2.html',{'form':form})