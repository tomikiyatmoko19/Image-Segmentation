import time 
import numpy as np
import cv2
import skimage

start = time.time()
img=cv2.imread('F:/New folder (6)/drive/09_test.tif')
#img=cv2.imread('F:/New folder (6)/datastare/im0005.ppm')
#cv2.imshow('input',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gamma= np.array(255*(gray/255)**0.9,dtype='uint8')
img3 = cv2.hconcat([gamma])
cv2.imshow('gamma',img3)

clahe = cv2.createCLAHE(clipLimit=7, tileGridSize=(10,10))
clah = clahe.apply(img3)
cv2.imshow('clahe',clah)


kernel_sharpening = np.array([[0,-1,0], 
                              [-1, 5,-1],
                              [0,-1,0]])

sharp=cv2.filter2D(clah, -1 , kernel_sharpening)
cv2.imshow('sharpen', sharp)
kernel = np.ones((2,2),np.float64)/25
average = cv2.filter2D(sharp,-1,kernel)
cv2.imshow('sharpen+smooth', average)

threshold_sauvola = skimage.filters.threshold_sauvola(average, window_size=11, k=0.17)
binary_threshold_sauvola = average > threshold_sauvola
indices = binary_threshold_sauvola.astype(np.uint8)  
indices*=255
inverse = cv2.bitwise_not(indices)
cv2.imshow('sauvola thres',inverse)

nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(inverse, connectivity=4)
sizes = stats[1:, -1]; 
nb_components1 = nb_components - 1
min_size = 40
hapuspixel = np.zeros((output.shape))
for i in range(0, nb_components1):
    if sizes[i] > min_size:
        hapuspixel[output == i + 1] = 255
hapuspixel= np.uint8(hapuspixel)
#cv2.imshow('hapus pixel kecil',hapuspixel)

#mask
gammaroi= np.array(255*(gray/255)**0.7,dtype='uint8')
gma = cv2.hconcat([gammaroi])
retval, mask_threshold = cv2.threshold(gma, 68, 500, cv2.THRESH_BINARY)
inverse_maskbang = cv2.bitwise_not(mask_threshold)
kernel3 = np.ones((5,5),np.uint8)
dilation = cv2.dilate(inverse_maskbang,kernel3,iterations = 1)
cv2.imshow('mask',dilation)

output5= hapuspixel-dilation
median = cv2.medianBlur(output5,3)
cv2.imshow('median',median)

kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
closing = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel2)
norm_image = cv2.normalize(closing, None, alpha = 0, beta = 1, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
output2=norm_image.astype(np.uint8)
output3 = cv2.normalize(output2, None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
cv2.imwrite('F:/New folder (6)/data uji/versi jpg/sauvola jp/DRIVE/09_test.jpg', output3) 
cv2.imshow('hasil',output3)
cv2.waitKey(0)
cv2.destroyAllWindows()
end = time.time()
print(end - start)