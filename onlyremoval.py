import numpy as np
import cv2

img = cv2.imread('um_000073.png')

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

num_s = 0
num_l = 0
mean_s = 0
mean_l = 0
var_s = 0
var_l = 0

#print(binary_img[20,56])

#print(img.shape[0])
#print(img.shape[1])

for i in range(0,img.shape[0]):
	for j in range(0,img.shape[1]):
		if hsv_img[i,j,0] > 97 and hsv_img[i,j,0] < 120:
		#if hsv_img[i,j,1] <= 30 or hsv_img[i,j,2] <= 30:
			#if binary_img[i,j] == 0:
			#if hsv_img[i,j,0] > 97 and hsv_img[i,j,0] < 120:
				mean_s += gray_img[i,j]
				num_s += 1
		else:
				mean_l += gray_img[i,j]
				num_l += 1

mean_s = mean_s / num_s
mean_l = mean_l / num_l

#print(mean_s)

for i in range(0,img.shape[0]):
	for j in range(0,img.shape[1]):
		if hsv_img[i,j,0] > 97 and hsv_img[i,j,0] < 120:
			#if hsv_img[i,j,1] <= 30 or hsv_img[i,j,2] <= 30:
				#if binary_img[i,j] == 0:
					var_s += (gray_img[i,j] - mean_s) ** 2
		else :
					var_l += (gray_img[i,j] - mean_l) ** 2

var_s = var_s / num_s
var_l = var_l / num_l

for i in range(0,img.shape[0]):
	for j in range(0,img.shape[1]):
		if hsv_img[i,j,0] > 97 and hsv_img[i,j,0] < 120:
		#if hsv_img[i,j,1] <= 30 and hsv_img[i,j,2] <=180:
			#print(hsv_img[i,j,2])
			if hsv_img[i,j,2] <= 200:
				#if binary_img[i,j] == 0:
					gray_img[i,j] -= (mean_s + ((gray_img[i,j] - mean_l) * var_l / var_s))/2.5 

kernel = np.ones((2, 2), np.uint8)

dilation2 = cv2.dilate(gray_img, kernel, iterations = 1)

median3 = cv2.medianBlur(dilation2, 3)

erosion3 = cv2.erode(median3, kernel, iterations = 1)

for i in range(0,img.shape[0]):
	for j in range(0,img.shape[1]):
		hsv_img[i,j,2] = erosion3[i,j]
#median2 = cv2.medianBlur(erosion3, 3)

#retval, threshold = cv2.threshold(erosion3,0,255,cv2.THRESH_OTSU)

cv2.imshow('Final image', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

