from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
	return render(request, 'website/index.html')



def about(request):
	return render(request,'website/about.html')



def projects(request):
	return render(request,'website/projects.html')