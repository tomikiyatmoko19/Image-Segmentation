import numpy as np
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt
import skimage.filters as segment
from skimage import morphology

img=cv2.imread('F:/New folder (6)/datastare/im0255.ppm')
#0cv2.imshow('input',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gamma= np.array(255*(gray/255)**0.8,dtype='uint8')
img3 = cv2.hconcat([gamma])
#cv2.imshow('gamma',img3)

clahe = cv2.createCLAHE(clipLimit=7, tileGridSize=(10,10))
cl1 = clahe.apply(img3)
#cv2.imshow('clahe',cl1)


kernel_sharpening = np.array([[0,-1,0], 
                              [-1,5,-1],
                              [0,-1,0]])

sharpened = cv2.filter2D(cl1, -1 , kernel_sharpening)
cv2.imshow('Peningkatan cit', sharpened)

kernel = np.ones((2,2),np.float64)/25
dst = cv2.filter2D(sharpened,-1,kernel)
cv2.imshow('Peningkatan citra', dst)

A = np.double(sharpened)
out = np.zeros(A.shape, np.double)
mat2gray = cv2.normalize(A, out, 1.0, 0.0, cv2.NORM_MINMAX)

dynamic= dst - mat2gray

window_size = 15
thresh_niblack = segment.threshold_niblack(dynamic, window_size=window_size, k=0.4)
binary_niblack = dynamic >= thresh_niblack

indices = binary_niblack.astype(np.uint8)  
indices*=255
#cv2.imshow('Indices',indices)
#
inverse = cv2.bitwise_not(indices)
#cv2.imshow('dynamic thres',inverse)

nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(inverse, connectivity=4)
sizes = stats[1:, -1]; nb_components = nb_components - 1
min_size = 350
img6 = np.zeros((output.shape))
for i in range(0, nb_components):
    if sizes[i] > min_size:
        img6[output == i + 1] = 255
img6= np.uint8(img6)
#cv2.imshow('bwareopen',img6)

#mask
gammaroi= np.array(255*(gray/255)**0.9,dtype='uint8')
gma = cv2.hconcat([gammaroi])
retval, mask_threshold = cv2.threshold(gma, 68, 500, cv2.THRESH_BINARY)
inverse_maskbang = cv2.bitwise_not(mask_threshold)
kernel3 = np.ones((5,5),np.uint8)
dilation = cv2.dilate(inverse_maskbang,kernel3,iterations = 1)
#cv2.imshow('mask',dilation)

output= img6-(np.uint8(dilation))
median = cv2.medianBlur(output,3)
#cv2.imshow('median',median)

kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
closing = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel2)

cv2.imshow('hasil',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('F:/New folder (6)/data uji\Pyth/01test.png', closing) 