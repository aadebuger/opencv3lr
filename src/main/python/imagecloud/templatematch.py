'''
Created on 2017年11月2日

@author: aadebuger
'''

import cv2
import numpy as np

img_rgb = cv2.imread('test3.jpg')
#

#small = cv2.resize(img_rgb, (0,0), fx=0.2, fy=0.2) 

#img_rgb = cv2.imread('/Users/aadebuger/Downloads/1109_1.jpg')

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('coin.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    print("rectangle")
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)
while True:
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
        

if __name__ == '__main__':
    pass