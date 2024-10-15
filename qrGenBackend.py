# Import QRCode from pyqrcode 
import pyqrcode 
import png 
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

def generate(name,url):
    name_png = name + ".png"
    name_svg = name + ".svg"
    qr = pyqrcode.create(url)
    qr.svg(name_svg, scale = 8)
    qr.png(name_png, scale = 6)