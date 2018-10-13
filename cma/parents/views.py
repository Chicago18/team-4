from django.shortcuts import render , redirect
from . forms import RegisterForm , HousingForm
from . utils import render_to_pdf
from django.template import Context, Template
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from . models import Household , Register
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




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
			return redirect('/house',pk=post.pk)
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


def generate_pdf(request,register_id):
	template = get_template ('parents/invoice.html')
	register = Register.objects.get(pk=register_id)
	context = {
	"register":register,
	"houshold":Household.objects.all()
	}
	html = template.render(context)
	pdf = render_to_pdf('parents/invoice.html',context)
	return HttpResponse(pdf,content_type='application/pdf')	
    
def logged_in(request):
	user = User.objects.all()
	context = {
	'users':user
	}
	return render(request,'parents/home.html',context)
   