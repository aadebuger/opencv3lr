#encoding=utf-8
'''
Created on 2017年11月9日

@author: aadebuger
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt
#img = cv2.imread('/Users/aadebuger/Downloads/1109_1.jpg')
img = cv2.imread('test1.jpg')
#cropimage = img[170:500,20:300]

mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#rect = (50,50,450,290)
#rect=(170,20,500,300)
#rect=(170,20,500,300)
rect=(20,200,300,500)


cropimage = img[200:500,20:300]
cv2.imwrite("coin.jpg",cropimage)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img1 = img*mask2[:,:,np.newaxis]
plt.imshow(img1),plt.colorbar(),plt.show()
   

if __name__ == '__main__':
    pass