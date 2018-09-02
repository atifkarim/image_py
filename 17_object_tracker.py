import cv2
import numpy as np

def main():
    
    #windowname='tracker'
    #cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
        
    else:
        ret=False
        
    while ret:
        ret,frame=cap.read()
        
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #green
        low_green=np.array([40,50,50]) 
        high_green=np.array([80,255,255])
        #blue
        low_blue=np.array([100,50,50])
        high_blue=np.array([140,255,255])
        
        #red
        low_red=np.array([0,100,100])
        high_red=np.array([10,255,255])
        
        image_mask_green=cv2.inRange(hsv,low_green,high_green)
        image_mask_blue=cv2.inRange(hsv,low_blue,high_blue)
        image_mask_red=cv2.inRange(hsv,low_red,high_red)
        
        image_mask=image_mask_green+image_mask_blue+image_mask_red
        
        #output_green=cv2.bitwise_and(frame,frame,mask=image_mask_green)
        #output_blue=cv2.bitwise_and(frame,frame,mask=image_mask_blue)
        #output_red=cv2.bitwise_and(frame,frame,mask=image_mask_red)
        
        output=cv2.bitwise_and(frame,frame,mask=image_mask)
        
        cv2.imshow("main webcam transmission",frame)
        
        cv2.imshow('mask',image_mask)
        
        #cv2.imshow("image mask_green",image_mask_green,"image mask_blue",image_mask_blue,"image mask_red",image_mask_red)
        
        
        #cv2.imshow('green_color tracker',output_green)
        #cv2.imshow('blue_color_tracker',output_blue)
        #cv2.imshow('red_color_tracker',output_red)
        #print(frame)
        
        cv2.imshow('color_tracker',output)
        
        #if cv2.waitKey(1)==27:
         #   break
        k = cv2.waitKey(5) & 0xFF
        if k==27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
main()