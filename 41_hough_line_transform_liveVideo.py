# -*- coding: utf-8 -*-
import cv2
import  numpy as np

def main():
    windowname='live video'
    cv2.namedWindow(windowname)
    
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
        
    else:
        ret=False
        
    while ret:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges=cv2.Canny(gray,50,250,apertureSize=5,L2gradient=True)
        lines=cv2.HoughLines(edges,1,np.pi/180,200)
        
        if lines is not None:
            for rho, theta in lines[0]:
                a=np.cos(theta)
                b=np.sin(theta)
                xo=a*rho
                yo=b*rho
                pts1=(int(xo+1000*(-b)),int(yo+1000*(a)))
                pts2=(int(xo-1000*(-b)),int(yo-1000*(a)))
                cv2.line(frame,pts1,pts2,(0,0,255),15)
        
        cv2.imshow(windowname,frame)
        #cv2.imshow('edge window',edges)
        
        print(edges)
        
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    
main()
