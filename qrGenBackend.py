# Import QRCode from pyqrcode 
import pyqrcode 
import os
from pyqrcode import QRCode 

'''
# String which represents the QR code 
s = ""

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the svg file naming "myqr.svg" 
url.svg("myqr.svg", scale = 8) 

# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6)''' 

#Generation function
script_dir = os.path.dirname(__file__)
IMG_DIRECTORY = os.path.join(script_dir, "generated-qrs")

FINAL_PNG_PATH = ''

def generate(name,url):
    if not os.path.exists(IMG_DIRECTORY):
        os.mkdir(IMG_DIRECTORY)
    name_png = name + ".png"
    name_svg = name + ".svg"
    global FINAL_PNG_PATH
    FINAL_PNG_PATH = os.path.join(IMG_DIRECTORY,name_png)
    print(FINAL_PNG_PATH)
    svg_path = os.path.join(IMG_DIRECTORY,name_svg)
    qr = pyqrcode.create(url)
    qr.svg(svg_path, scale = 8)
    qr.png(FINAL_PNG_PATH, scale =6)

def path():
    return FINAL_PNG_PATH