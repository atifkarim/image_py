# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

def main():
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
        print(ret)
        print(frame)
    else:
        ret=False
        
    img=cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    plt.imshow(img)
    plt.title('captured img by webcam')
    plt.show()
    
    
    cap.release()
    
main()
