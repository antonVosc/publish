import qrcode

img = qrcode.make('My first QR')
img.save('QR.png')