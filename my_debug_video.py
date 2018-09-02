# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
         ret,frame=cap.read()
    else:
         ret=False
    
    ret,frame1=cap.read()
    ret,frame2=cap.read()
         
    while ret:
        
        #ret,frame=cap.read()
        cv2.imshow('1st',frame1)
        cv2.imshow('2nd',frame2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
main()
