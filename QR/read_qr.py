import cv2

img = cv2.imread('QR.png')
detection = cv2.QRCodeDetector()
val, pts, st_code = detection.detectAndDecode(img)
print(val)