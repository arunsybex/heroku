from PIL import Image
from pytesser import *
import os

image_file = 'fnord.tif'
im = Image.open(image_file)
text = image_to_string(im)
text = image_file_to_string(image_file)
text = image_file_to_string(image_file, graceful_errors=True)
print text
