from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/Karan Joshi/Desktop/CODE/Github/My own/Python-Projects-for-Beginners/08 QR code encoder & decoder/Saved Image/Image-1.png")
text = decode(img)
print(text)