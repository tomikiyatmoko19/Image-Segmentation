# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:44:50 2019

@author: Reimu
"""

import time 
import numpy as np
import cv2
import skimage

start = time.time()
#img=cv2.imread('F:/New folder (6)/drive/01_test.tif')
img=cv2.imread('F:/New folder (6)/datastare/im0162.ppm')
#cv2.imshow('input',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gamma= np.array(255*(gray/255)**0.9,dtype='uint8')
img3 = cv2.hconcat([gamma])
cv2.imshow('gamma',img3)

clahe = cv2.createCLAHE(clipLimit=7, tileGridSize=(10,10))
cl1 = clahe.apply(img3)
cv2.imshow('clahe',cl1)


kernel_sharpening = np.array([[0,-1,0], 
                              [-1, 5,-1],
                              [0,-1,0]])

sharp=cv2.filter2D(cl1, -1 , kernel_sharpening)
cv2.imshow('sharpen', sharp)
#kernel = np.ones((2,2),np.float64)/25
#dst = cv2.filter2D(sharp,-1,kernel)
#cv2.imshow('sharpen+smooth', dst)

threshold_sauvola = skimage.filters.threshold_sauvola(sharp, window_size=11, k=0.17)
binary_threshold_sauvola = sharp > threshold_sauvola
indices = binary_threshold_sauvola.astype(np.uint8)  
indices*=255
cv2.imshow('Indices',indices)
inverse = cv2.bitwise_not(indices)
cv2.imshow('sauvola',inverse)

nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(inverse, connectivity=4)
sizes = stats[1:, -1]; 
nb_components1 = nb_components - 1
min_size = 40
img6 = np.zeros((output.shape))
for i in range(0, nb_components1):
    if sizes[i] > min_size:
        img6[output == i + 1] = 255
img6= np.uint8(img6)
cv2.imshow('bwareopen',img6)

#mask
gammaroi= np.array(255*(gray/255)**0.7,dtype='uint8')
gma = cv2.hconcat([gammaroi])
retval, mask_threshold = cv2.threshold(gma, 68, 500, cv2.THRESH_BINARY)
inverse_maskbang = cv2.bitwise_not(mask_threshold)
kernel3 = np.ones((5,5),np.uint8)
dilation = cv2.dilate(inverse_maskbang,kernel3,iterations = 1)
cv2.imshow('mask',dilation)

output= img6-dilation
median = cv2.medianBlur(output,3)
cv2.imshow('median',median)

kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
closing = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel2)
norm_image = cv2.normalize(closing, None, alpha = 0, beta = 1, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
output2=norm_image.astype(np.uint8)
output3 = cv2.normalize(output2, None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
#cv2.imwrite('F:/New folder (6)/data uji\Pyth/im0324.png', output3) 
cv2.imshow('hasil',output3)
cv2.waitKey(0)
cv2.destroyAllWindows()
end = time.time()
print(end - start)