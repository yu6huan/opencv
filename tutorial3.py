import cv2
import numpy as np

kernel = np.ones((10, 10), np.uint8)
kernel1 = np.ones((10, 10), np.uint8)


img = cv2.imread('colorcolor.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (15, 15), 10)
canny = cv2.Canny(img, 200, 250)
dilate = cv2.dilate(canny, kernel, iterations=2)
erode = cv2.erode(dilate, kernel1, iterations=2)


# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)
