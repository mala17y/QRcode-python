import qrcode as qr  
img = qr.make("https://www.linkedin.com/feed/")
img.save("qrcode.png")


'''
qr code is a library of python to make qr codes
 we use here make function to make qr code
 and save to save it
 '''