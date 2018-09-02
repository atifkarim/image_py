# -*- coding: utf-8 -*-
import cv2

def main():
    windowname='live video'
    cv2.namedWindow(windowname)
    
    graywindow='gray'
    cv2.namedWindow(graywindow)
    cap=cv2.VideoCapture(0)
    
    filename="/home/atif/spyder_project/youtube_ashwin_tutorial/output video/output.mp4"
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=30
    resolution=(640,480)
    videooutput=cv2.VideoWriter(filename,codec,framerate,resolution)
    
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
        
    while ret:
        ret,frame=cap.read()
        
        videooutput.write(frame)
        #output=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #output1=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        cv2.imshow(windowname,frame)
       # cv2.imshow(graywindow,output)
       # cv2.imshow('new one',output1)
        
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    videooutput.release()
    cap.release()
    
main()
# -*- coding: utf-8 -*-

