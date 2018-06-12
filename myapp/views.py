from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from PIL import Image
from pytesser import *
import os,shutil
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
	if request.method == "GET":
		# image_file = '/home/arunkumar/projects/heroku/myapp/fnord.tif'
		# im = Image.open(image_file)
		# text = image_to_string(im)
		# text = image_file_to_string(image_file)
		# text = image_file_to_string(image_file, graceful_errors=True)
		# print text
		return render(request,'index.html');
	elif request.method == "POST":
		crfs_mid = request.POST["csrfmiddlewaretoken"];
		output = "";
		if request.method == 'POST' and request.FILES['file']:
			for wfile in request.FILES.getlist('file'):
				myfile = wfile
				fs = FileSystemStorage()
				filename = fs.save(crfs_mid+"/"+myfile.name, myfile)
				uploaded_file_url = fs.url(filename)
				image_file = str(settings.BASE_DIR)+str(uploaded_file_url)
				im = Image.open(image_file)
				text = image_to_string(im)
				text = image_file_to_string(image_file)
				text = image_file_to_string(image_file, graceful_errors=True)
				output = output + text
		shutil.rmtree(settings.BASE_DIR+'/media/'+crfs_mid)
		return HttpResponse(output)
