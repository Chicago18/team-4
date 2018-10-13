from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
	return render(request,"parents/index.html")

def grades(request):
	return render(request,"parents/grades.html")