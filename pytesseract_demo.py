# https://pypi.org/project/pytesseract/#installation
image_input_folder = "input_images"

from PIL import Image
from pytesseract import image_to_string
import os

input_image_names = os.listdir(image_input_folder)
for filename in input_image_names:
    img = Image.open(f"./{image_input_folder}/{filename}")
    img_text = image_to_string(img)
    
    print(f"========== BEGIN {filename} ==========")
    print(img_text)
    print(f"========== END {filename} ==========")
