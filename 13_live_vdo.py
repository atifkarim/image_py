# -*- coding: utf-8 -*-
import cv2

def main():
    windowname='live video'
    cv2.namedWindow(windowname)
    
    graywindow='gray'
    cv2.namedWindow(graywindow)
    cap=cv2.VideoCapture(0)
    
    #cap.set(3,104)
    #cap.set(4,76)
    
    print('width: '+str(cap.get(3)))
    print('width: '+str(cap.get(4)))
    
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
        
    while ret:
        ret,frame=cap.read()
        output=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        output1=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        cv2.imshow(windowname,frame)
        cv2.imshow(graywindow,output)
        cv2.imshow('new one',output1)
        
        '''if cv2.waitKey(1)==27:'''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
main()
