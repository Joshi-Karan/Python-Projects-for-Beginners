# Code has been comment to avoid conflict while re-testing

import qrcode 

# Enter data below
data = "Hey If you love this repo, do star it"

# Making Simple Qr code and saving it
'''
img = qrcode.make(data)
img.save("C:/Users/Karan Joshi/Desktop/CODE/Github/My own/Python-Projects-for-Beginners/08 QR code encoder & decoder/Saved Image/Image-1.png")
'''

# Playing with it
'''
qr = qrcode.QRCode(
    # For details read module https://pypi.org/project/qrcode/
    version = 1,   
    box_size = 10,  
    border = 5
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = "white", back_color = "black")

img.save("C:/Users/Karan Joshi/Desktop/CODE/Github/My own/Python-Projects-for-Beginners/08 QR code encoder & decoder/Saved Image/Image-2.png")
'''