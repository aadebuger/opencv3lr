'''
Created on 2017年11月13日

@author: aadebuger
'''
import numpy as np
import cv2
#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_bg_subtraction/py_bg_subtraction.html

def func1():


        
        cap = cv2.VideoCapture('vtest.avi')
        
        fgbg = cv2.createBackgroundSubtractorMOG()
        
        while(1):
            ret, frame = cap.read()
        
            fgmask = fgbg.apply(frame)
        
            cv2.imshow('frame',fgmask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    pass