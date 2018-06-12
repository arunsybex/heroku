from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from PIL import Image
from pytesser import *
import os

# Create your views here.

def index(request):
	if request.method == "GET":
		# image_file = '/home/mnwsoftware/projects/heroku/myapp/fnord.tif'
		# im = Image.open(image_file)
		# text = image_to_string(im)
		# text = image_file_to_string(image_file)
		# text = image_file_to_string(image_file, graceful_errors=True)
		# print text
		return render(request,'index.html');
	elif request.method == "POST":
		crfs_mid = request.POST["csrfmiddlewaretoken"];
		print request.FILES.getlist('file')
		for wfile in request.FILES.getlist('file'):
			im = Image.open(wfile)
			text = image_to_string(im)
			# text = image_file_to_string(im)
			# text = image_file_to_string(im, graceful_errors=True)
			print text
		return render(request,'index.html');
