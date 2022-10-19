import cv2
import numpy as np

o = cv2.imread('capture.jpg')
im_grey = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY) # 灰階影像
t, binary_img = cv2.threshold(im_grey, 150, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)
for i in range(n):
    x,y,w,h = cv2.boundingRect(contours[i])
    brcnt = np.array([[[x, y]], [[x+w, y]], [[x+w, y+h]], [[x, y+h]]])
    cv2.drawContours(o, [brcnt], -1, (0, 0, 255), 2)

cv2.imshow('frame', o)
cv2.waitKey()
cv2.destroyAllWindows()