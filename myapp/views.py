from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def index(request):
	if request.method == "GET":
		return render(request,'index.html');
	elif request.method == "POST":
		return render(request,'index.html');
