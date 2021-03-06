# -*- coding: utf-8 -*-
import cv2
import numpy as np

def empty():
    pass

def main():
    img1=np.zeros((512,512,3),np.uint8)
    windowname="open cv BGR color palette"
    cv2.namedWindow(windowname)
    
    cv2.createTrackbar('B',windowname,0,255,empty)
    cv2.createTrackbar('G',windowname,0,255,empty)
    cv2.createTrackbar('R',windowname,0,255,empty)
    
    while(True):
        cv2.imshow(windowname,img1)
        
        if cv2.waitKey(1)==27:
            break
        blue=cv2.getTrackbarPos('B',windowname)
        green=cv2.getTrackbarPos('G',windowname)
        red=cv2.getTrackbarPos('R',windowname)
        
        img1[:]=[blue,green,red]
        #print(blue,green,red)

main()

